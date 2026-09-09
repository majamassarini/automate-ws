import aiohttp_jinja2
from ws.i18n import get_locale, make_translator
import home.scheduler.trigger.protocol
import home.scheduler.trigger.protocol.delay
import home.scheduler.trigger.protocol.multi
import home.scheduler.trigger.state
import home.scheduler.trigger.state.delay

from ws.handler.appliance import Handler as Parent
from ws.handler.event import registry as event_registry


def _event_str(event):
    if hasattr(event, "name"):
        return f"{type(event).__module__}.{type(event).__name__}.{event.name}"
    return f"{type(event).__module__}.{type(event).__name__}"


def _event_display(event):
    if hasattr(event, "name"):
        return f"{type(event).__module__}.{type(event).__name__}.{event.name}"
    type_str = f"{type(event).__module__}.{type(event).__name__}"
    value = str(event).strip()
    return f"{type_str} ({value})" if value else type_str


def _protocol_trigger_performer_details(trigger, inner_trigger_to_performer):
    """Return performer-name detail entries for protocol triggers.

    Multi triggers expose four inner triggers (_positive_a, _negative_a,
    _positive_b, _negative_b); all others use a single _protocol_trigger.
    """
    details = []
    if isinstance(trigger, home.scheduler.trigger.protocol.multi.Trigger):
        for pt, label in [
            (trigger._positive_a, "Triggered by (A+)"),
            (trigger._negative_a, "Reset by (A-)"),
            (trigger._positive_b, "Triggered by (B+)"),
            (trigger._negative_b, "Reset by (B-)"),
        ]:
            name = inner_trigger_to_performer.get(id(pt))
            if name:
                details.append({"label": label, "value": name})
    elif isinstance(trigger, home.scheduler.trigger.protocol.Trigger):
        name = inner_trigger_to_performer.get(id(trigger._protocol_trigger))
        if name:
            details.append({"label": "Triggered by performer", "value": name})
    return details


def _trigger_events(trigger):
    """Return the effective events for a trigger.

    Delay triggers (state.delay and protocol.delay subclasses) carry their
    events inside the Delay helper object rather than on trigger.events
    itself (which is always []). Fall back to _delay._scheduler_trigger_events
    when trigger.events is empty.

    Crawler triggers may perform network I/O inside the events property; any
    exception is silenced so that a transient network error never breaks the
    detail page.
    """
    try:
        events = list(trigger.events)
    except Exception:
        events = []
    if not events and isinstance(
        trigger,
        (
            home.scheduler.trigger.state.delay.Trigger,
            home.scheduler.trigger.protocol.delay.Trigger,
        ),
    ):
        events = list(trigger._delay._scheduler_trigger_events)
    return events


class Handler(Parent):

    ENCODING = "utf-8"

    def get_performers(self, appliance):
        performers = list()
        for performer in self._home_resources.brain_performers:
            if performer.appliance.name == appliance.name:
                performers.append(performer)
        return performers

    def get_group_of_performers(self, appliance):
        groups = {}
        all_group_performers = set()
        for (
            key,
            value,
        ) in self._home_resources.brain_group_of_performers.items():
            for performer in value:
                if performer.appliance.name == appliance.name:
                    groups[key] = list(value)
                    all_group_performers.update(value)
                    break
        return groups, all_group_performers

    @staticmethod
    def _is_reactive_trigger(trigger, direct_performer_inner_triggers):
        if isinstance(trigger, home.scheduler.trigger.state.Trigger):
            return True
        if isinstance(trigger, home.scheduler.trigger.protocol.Trigger):
            if (
                id(trigger._protocol_trigger)
                in direct_performer_inner_triggers
            ):
                return True
        return False

    def get_scheduler_triggers(self, group_of_performers, direct_performers):
        from ws.handler.scheduler import registry as scheduler_registry

        inner_trigger_to_performer = {
            id(t): p.name
            for p in self._home_resources.brain_performers
            for t in p.triggers
        }
        direct_set = set(direct_performers)
        direct_performer_inner_triggers = {
            id(t) for p in direct_performers for t in p.triggers
        }
        seen = set()
        reactive = []
        scheduled = []
        for performers, triggers in self._home_resources.brain_schedule_infos:
            relevant = set(performers).intersection(direct_set)
            if relevant:
                for trigger in triggers:
                    if id(trigger) in seen:
                        continue
                    seen.add(id(trigger))
                    mod = type(trigger).__module__
                    kind = ".".join(mod.split(".")[-2:]) if "." in mod else mod
                    details = []
                    handler_class = scheduler_registry.mapper.get(
                        type(trigger)
                    )
                    if handler_class:
                        h = handler_class()
                        kind = h.get_kind(trigger)
                        details = h.get_details(trigger)
                    triggered_by = _protocol_trigger_performer_details(
                        trigger, inner_trigger_to_performer
                    )
                    details = triggered_by + details
                    evts = _trigger_events(trigger)
                    entry = {
                        "name": trigger.name,
                        "kind": kind,
                        "performers": [str(p) for p in relevant],
                        "events": [_event_str(e) for e in evts],
                        "event_displays": [_event_display(e) for e in evts],
                        "details": details,
                        "_trigger": trigger,
                    }
                    if self._is_reactive_trigger(
                        trigger, direct_performer_inner_triggers
                    ):
                        reactive.append(entry)
                    else:
                        scheduled.append(entry)
        return reactive, scheduled

    def get_event_beans_with_str(self, appliance):
        beans = []
        appliance_handler = self.get_appliance_handler(appliance)
        for num, event in enumerate(appliance.events):
            handler = self.get_event_handler(appliance, event)
            if handler:
                bean = handler.get(event)
                appliance_id = self.get_html_id(appliance.name)
                bean.set_enabled(appliance, event)
                bean.set_id(appliance_id, num)
                bean.set_id_enabled(appliance_id, num)
                bean.set_id_icon(appliance_id, num)
                bean.set_id_label(appliance_id, num)
                bean.set_is_displayed(
                    appliance_handler.is_displayed(appliance, event)
                )
                bean.event_str = _event_str(event)
                beans.append(bean)
        beans.reverse()
        return beans

    def get_event_panel_items(self, appliance, translator):
        """Return (description, icon, enabled) for every event in the appliance.

        Same format as the history page's all_event_details so the shared
        event_state_panel.html renders identical rows in both places.
        """
        items = []
        for event in appliance.events:
            try:
                handler_cls = event_registry.mapper[
                    self.get_registry_key(appliance, event)
                ]
            except KeyError:
                try:
                    handler_cls = event_registry.mapper[
                        self.get_registry_key(None, event)
                    ]
                except KeyError:
                    handler_cls = None
            if handler_cls:
                h = handler_cls.with_translator(
                    self._home_resources, translator
                )
                desc = h.get_description_for_history(event) or ""
                icon = h.get_icon(event)
                enabled = appliance.is_enabled(event)
                if desc or (icon and icon != ""):
                    items.append((desc, icon, enabled))
        return items

    async def _get_response_data(self, request, appliance):
        performers = self.get_performers(appliance)
        groups, all_group_performers = self.get_group_of_performers(appliance)
        reactive_triggers, scheduled_triggers = self.get_scheduler_triggers(
            all_group_performers, performers
        )
        await self._home_resources.redis_gateway.update(appliance)
        translator = make_translator(get_locale(request))
        bean = self.get_appliance_bean(appliance)
        event_beans = self.get_event_beans_with_str(appliance)
        event_panel_items = self.get_event_panel_items(appliance, translator)
        collection = self._home_resources.appliances.collection_for(appliance)
        collection_url = request.app.router["collection"].url_for(
            name=collection
        )
        history_url = request.app.router["history"].url_for(
            name=appliance.name
        )
        user = await self.get_user(request)
        trigger_performers = []
        command_performers = []
        for performer in performers:
            p_groups = [
                group_name
                for group_name, group_performers_list in groups.items()
                if group_name != performer.name
                and any(
                    gp is performer or gp.name == performer.name
                    for gp in group_performers_list
                )
            ]
            if performer.triggers:
                performer_events = sorted(
                    {
                        _event_str(e)
                        for t in performer.triggers
                        for e in t.events
                    }
                )
                trigger_event_strs = [
                    (t, [_event_display(e) for e in t.events])
                    for t in performer.triggers
                ]
                trigger_performers.append(
                    (performer, p_groups, performer_events, trigger_event_strs)
                )
            if performer.commands:
                command_performers.append((performer, p_groups))

        ctx = {
            "user": user,
            "appliance": appliance,
            "id": self.get_html_id(appliance.name),
            "appliance_url": request.app.router["appliance"].url_for(
                name=appliance.name
            ),
            "collection_url": collection_url,
            "history_url": history_url,
            "collection": collection,
            "bean": bean,
            "event_beans": event_beans,
            "event_panel_items": event_panel_items,
            "trigger_performers": trigger_performers,
            "command_performers": command_performers,
            "reactive_triggers": reactive_triggers,
            "scheduled_triggers": scheduled_triggers,
        }
        return self.localize_context(request, ctx)

    @aiohttp_jinja2.template("details.html")
    async def get(self, request):
        appliance = await self.get_appliance(request)
        response_data = await self._get_response_data(request, appliance)
        return response_data
