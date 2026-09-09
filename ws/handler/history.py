import datetime
import logging
from typing import Optional
import aiohttp_jinja2
from home.scheduler.trigger.protocol import Trigger as _ProtocolTrigger
from home.scheduler.trigger.state import Trigger as _StateTrigger
from ws.handler.details import Handler as Parent, _event_display, _event_str
from ws.handler.event import registry
from ws.i18n import make_format_ts, make_translator


def _is_time_plausible(
    trigger, timestamp: float, window_seconds: float = 300
) -> bool:
    """Return True if *trigger* could plausibly have fired at *timestamp*.

    State and protocol triggers fire on appliance or bus events, not on
    a clock schedule, so they are always considered plausible.

    For time-scheduled triggers (cron, interval, sun, circadian …) we ask
    APScheduler whether the trigger would have fired within *window_seconds*
    of *timestamp*.  If ``get_next_fire_time`` finds a fire time inside
    [timestamp − window, timestamp + window] the trigger is plausible.
    """
    if isinstance(trigger, (_StateTrigger, _ProtocolTrigger)):
        return True
    try:
        tz = getattr(trigger, "_timezone", None)
        if tz is None:
            return True
        ts_dt = datetime.datetime.fromtimestamp(timestamp, tz=tz)
        window = datetime.timedelta(seconds=window_seconds)
        fire_time = trigger.get_next_fire_time(ts_dt - window, ts_dt - window)
        return fire_time is not None and fire_time <= ts_dt + window
    except Exception:
        return True


def _state_label(snapshot) -> str:
    """Return the computed state string for an appliance snapshot, or ''."""
    if snapshot is None or isinstance(snapshot, dict):
        return ""
    try:
        return snapshot.state.compute()
    except Exception:
        return ""


def _state_end_ts(history, idx) -> Optional[float]:
    """Return the timestamp when the state at *idx* ended.

    *history* is newest-first.  The state at *idx* ended at the first
    more-recent entry (lower index) whose computed state label differs.
    Returns ``None`` when *idx* == 0 (still the current state).
    """
    if idx == 0:
        return None
    current = _state_label(history[idx][1])
    for j in range(idx - 1, -1, -1):
        if _state_label(history[j][1]) != current:
            return float(history[j][0])
    return None


def _state_start_ts(history, idx) -> float:
    """Return the timestamp of the oldest entry with the same state.

    Scans forward (higher indices = older entries) to find the earliest
    contiguous entry that shares the state label, giving the true start of
    the state period regardless of intermediate event-value saves.
    """
    current = _state_label(history[idx][1])
    start = float(history[idx][0])
    for j in range(idx + 1, len(history)):
        if _state_label(history[j][1]) != current:
            break
        start = float(history[j][0])
    return start


def _format_duration(seconds: float) -> str:
    s = int(seconds)
    if s < 60:
        return f"{s}s"
    m, s = divmod(s, 60)
    if m < 60:
        return f"{m}m {s}s" if s else f"{m}m"
    h, m = divmod(m, 60)
    if h < 24:
        return f"{h}h {m}m" if m else f"{h}h"
    d, h = divmod(h, 24)
    return f"{d}d {h}h" if h else f"{d}d"


class Handler(Parent):

    PAGE_SIZE = 20

    def _build_causal_map(self, appliance):
        """Return {event_str: [trigger_entry, ...]} for this appliance.

        First pass: scheduler trigger entries (full metadata, time-filtered).

        Second pass: for event strings with no scheduler trigger, scan every
        performer's own protocol triggers.  This covers forced events that
        arrive directly from a KNX button without a matching !protocol.Trigger
        entry in the scheduler_triggers YAML.  These entries carry
        _trigger=None so _is_time_plausible always passes them through.
        """
        performers = self.get_performers(appliance)
        _, all_group = self.get_group_of_performers(appliance)
        reactive, scheduled = self.get_scheduler_triggers(
            all_group, performers
        )
        causal_map: dict = {}
        for entry in reactive + scheduled:
            for ev_str in entry["events"]:
                causal_map.setdefault(ev_str, []).append(entry)

        # Fallback: performer protocol triggers for uncovered events
        seen_fallback: set = set()
        for performer in all_group:
            for pt in performer.triggers:
                for event in pt.events:
                    ev_str = _event_str(event)
                    if ev_str in causal_map:
                        continue
                    key = (ev_str, performer.name)
                    if key in seen_fallback:
                        continue
                    seen_fallback.add(key)
                    causal_map.setdefault(ev_str, []).append(
                        {
                            "name": performer.name,
                            "kind": "Direct input",
                            "performers": [],
                            "events": [ev_str],
                            "event_displays": [_event_display(event)],
                            "details": [
                                {
                                    "label": "Triggered by performer",
                                    "value": performer.name,
                                }
                            ],
                            "_trigger": None,
                        }
                    )
        return causal_map

    async def _process_raw_history(
        self, appliance, history, translator, format_ts=None
    ):
        if format_ts is None:
            format_ts = make_format_ts("en")
        causal_map = self._build_causal_map(appliance)
        history_strs = list()
        for idx, (timestamp, old_appliance) in enumerate(history):
            if isinstance(old_appliance, dict):
                skip = True
            else:
                skip = False

            # Duration: find the first more-recent entry where the computed
            # state label differs.  Ignores saves that only changed event
            # values (e.g. brightness) while the state stayed the same.
            end_ts = _state_end_ts(history, idx)
            duration = (
                _format_duration(end_ts - _state_start_ts(history, idx))
                if end_ts is not None
                else None
            )

            # Changed events: history[idx+1] is the previous (older) state.
            try:
                events = old_appliance - history[idx + 1][1]
            except IndexError:
                events = set()
            except TypeError as e:
                logging.getLogger(__name__).error(
                    "{} for appliance {}".format(e, appliance)
                )
                events = set()
                skip = True

            all_event_details = list()
            if not isinstance(old_appliance, dict):
                for event in old_appliance.events:
                    changed = event in events
                    try:
                        handler = registry.mapper[
                            self.get_registry_key(appliance, event)
                        ]
                    except KeyError:
                        try:
                            handler = registry.mapper[
                                self.get_registry_key(None, event)
                            ]
                        except KeyError:
                            handler = None
                            if changed:
                                skip = True

                    if handler:
                        h = handler.with_translator(
                            self._home_resources, translator
                        )
                        event_description = h.get_description_for_history(
                            event
                        )
                        event_icon = h.get_icon(event)
                        all_event_details.append(
                            (event_description, event_icon, changed)
                        )

            seen = set()
            causal_links = []
            ts = float(timestamp)
            for event in events:
                for entry in causal_map.get(_event_str(event), []):
                    if id(entry) not in seen and _is_time_plausible(
                        entry.get("_trigger"), ts
                    ):
                        seen.add(id(entry))
                        causal_links.append(entry)

            if not skip:
                history_strs.append(
                    (
                        format_ts(float(timestamp)),
                        old_appliance,
                        self.get_appliance_bean(old_appliance),
                        all_event_details,
                        duration,
                        causal_links,
                    )
                )

        return history_strs

    async def get_history_page(
        self, appliance, offset, limit, translator, format_ts=None
    ):
        raw = await self._home_resources.redis_gateway.get_history(
            appliance, offset + limit + 1
        )
        processed = await self._process_raw_history(
            appliance, raw, translator, format_ts
        )
        page = processed[offset : offset + limit]
        has_more = len(processed) > offset + limit
        return page, has_more

    async def get_history_range_page(
        self,
        appliance,
        start_ts,
        end_ts,
        offset,
        limit,
        translator,
        format_ts=None,
    ):
        raw = await self._home_resources.redis_gateway.get_history_range(
            appliance, start_ts, end_ts
        )
        processed = await self._process_raw_history(
            appliance, raw, translator, format_ts
        )
        page = processed[offset : offset + limit]
        has_more = len(processed) > offset + limit
        return page, has_more

    @staticmethod
    def _resolve_filter(filter_name, from_date="", to_date=""):
        """Return (start_ts, end_ts) for a named preset, or None for 'all'.

        For 'custom', parse *from_date* and *to_date* as ISO date strings
        (YYYY-MM-DD).  Missing or invalid dates default to today / now.
        """
        now = datetime.datetime.now()
        midnight = now.replace(hour=0, minute=0, second=0, microsecond=0)
        if filter_name == "today":
            return midnight.timestamp(), now.timestamp()
        if filter_name == "yesterday":
            prev = midnight - datetime.timedelta(days=1)
            return prev.timestamp(), midnight.timestamp()
        if filter_name == "custom":
            try:
                start = datetime.datetime.strptime(from_date, "%Y-%m-%d")
            except (ValueError, TypeError):
                start = midnight
            try:
                end = datetime.datetime.strptime(to_date, "%Y-%m-%d")
                end = end.replace(hour=23, minute=59, second=59)
            except (ValueError, TypeError):
                end = now
            return start.timestamp(), end.timestamp()
        return None

    async def _build_context(self, request, appliance, offset, limit):
        from ws.i18n import get_locale

        locale = get_locale(request)
        format_ts = make_format_ts(locale)
        translator = make_translator(locale)
        filter_name = request.rel_url.query.get("filter", "all")
        from_date = request.rel_url.query.get("from_date", "")
        to_date = request.rel_url.query.get("to_date", "")
        ts_range = self._resolve_filter(filter_name, from_date, to_date)
        if ts_range:
            history, has_more = await self.get_history_range_page(
                appliance,
                ts_range[0],
                ts_range[1],
                offset,
                limit,
                translator,
                format_ts,
            )
        else:
            history, has_more = await self.get_history_page(
                appliance, offset, limit, translator, format_ts
            )
        collection = self._home_resources.appliances.collection_for(appliance)
        collection_url = request.app.router["collection"].url_for(
            name=collection
        )
        history_url = request.app.router["history"].url_for(
            name=appliance.name
        )
        user = await self.get_user(request)
        ctx = {
            "user": user,
            "appliance": appliance,
            "id": self.get_html_id(appliance.name),
            "appliance_uri": request.app.router["appliance"].url_for(
                name=appliance.name
            ),
            "history": history,
            "has_more": has_more,
            "offset": offset,
            "limit": limit,
            "next_offset": offset + limit,
            "collection_url": collection_url,
            "collection": collection,
            "history_url": history_url,
            "active_filter": filter_name,
            "custom_from": from_date,
            "custom_to": to_date,
        }
        return self.localize_context(request, ctx)

    @aiohttp_jinja2.template("history.html")
    async def get(self, request):
        offset = int(request.rel_url.query.get("offset", 0))
        limit = int(request.rel_url.query.get("limit", self.PAGE_SIZE))
        appliance = await self.get_appliance(request)
        context = await self._build_context(request, appliance, offset, limit)
        if request.headers.get("HX-Request"):
            return aiohttp_jinja2.render_template(
                "history_partial.html", request, context
            )
        return context
