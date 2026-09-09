"""Lightweight i18n support for automate-ws.

Language is determined once per request from the Accept-Language header.
Use ``i18n_context(request)`` to obtain the dict that every handler
merges into its template context:

    ctx.update(i18n_context(request))

Inside Jinja2 templates use ``{{ _("string") }}`` for translations and
``{{ format_ts(timestamp_float) }}`` for locale-aware datetime rendering.
"""

import datetime
import time as _time

# ---------------------------------------------------------------------------
# Italian translations
# ---------------------------------------------------------------------------

_IT: dict[str, str] = {
    # navbar
    "Home": "Home",
    "Collections": "Collezioni",
    "Logs": "Log",
    # auth
    "Login": "Accedi",
    "Username": "Utente",
    "Password": "Password",
    "Remember me for 30 days": "Ricordami per 30 giorni",
    "Logout": "Esci",
    # breadcrumbs
    "history": "cronologia",
    "details": "dettagli",
    # collection / collections
    "Copy name": "Copia nome",
    # history filters
    "Today": "Oggi",
    "Yesterday": "Ieri",
    # history entries
    "Possible triggers": "Possibili attivatori",
    "Load more": "Carica altro",
    # send modal
    "What to send for": "Cosa inviare per",
    "Enable/disable status (currently:": "Stato abilitazione (attualmente:",
    "enabled": "abilitato",
    "disabled": "disabilitato",
    "Event value (currently:": "Valore evento (attualmente:",
    "Appliances to send to:": "Dispositivi a cui inviare:",
    "All": "Tutti",
    "None": "Nessuno",
    "No other similar appliances found.": "Nessun altro dispositivo simile trovato.",
    "Send": "Invia",
    # details page sections
    "Outputs": "Uscite",
    "commands sent to physical devices": "comandi inviati ai dispositivi fisici",
    "Inputs": "Ingressi",
    "signals received from sensors & events": "segnali ricevuti da sensori ed eventi",
    "Performers": "Esecutori",
    "Triggers": "Trigger",
    "Notifies performer": "Notifica l'esecutore",
    "Sends": "Invia",
    "Details": "Dettagli",
    "Triggered via": "Attivato tramite",
    # trigger detail labels (used via _(detail.label) in templates)
    "Triggered by performer": "Attivato dall'esecutore",
    "Triggered by (A+)": "Attivato (A+)",
    "Reset by (A-)": "Resettato (A-)",
    "Triggered by (B+)": "Attivato (B+)",
    "Reset by (B-)": "Resettato (B-)",
    "Condition A": "Condizione A",
    "Condition B": "Condizione B",
    "Direct input": "Ingresso diretto",
    "Address": "Indirizzo",
    "Timeout": "Scadenza",
    "Selected": "Selezionato",
    "Direction": "Direzione",
    "Threshold": "Soglia",
    "Samples": "Campioni",
    "Min": "Min",
    "Max": "Max",
    "Stop notifies": "Ferma notifiche",
    "Latitude": "Latitudine",
    "Longitude": "Longitudine",
    "Elevation": "Altitudine",
    "Altitude": "Altezza",
    "Azimuth": "Azimut",
    "Events/day": "Eventi/giorno",
    "Interval": "Intervallo",
    "State": "Stato",
    "Run date": "Data esecuzione",
    "Enabled": "Abilitato",
    "Schedule": "Pianificazione",
    "Zone": "Zona",
    "Probability": "Probabilità",
    "from state duration": "dalla durata dello stato",
    # trigger kinds (used via _(trigger.kind) in templates)
    "Protocol": "Protocollo",
    "Protocol Delay": "Protocollo ritardato",
    "Protocol Enum": "Protocollo enum",
    "Protocol Mean >": "Protocollo media >",
    "Protocol Mean <": "Protocollo media <",
    "Protocol Mean ↔": "Protocollo media ↔",
    "Protocol Multi": "Protocollo multiplo",
    "Protocol Timer": "Protocollo timer",
    "Sunrise": "Alba",
    "Sunset": "Tramonto",
    "Sunhit": "Sole sul vetro",
    "Sun Left": "Sole scomparso",
    "Civil Sunrise": "Alba civile",
    "Civil Sunset": "Tramonto civile",
    "Astronomical Sunrise": "Alba astronomica",
    "Astronomical Sunset": "Tramonto astronomico",
    "Circadian": "Ritmo circadiano",
    "Cron": "Pianificato",
    "Date": "Data",
    "Rain On": "Pioggia attiva",
    "Rain Off": "Pioggia cessata",
    "Entering State": "Ingresso stato",
    "Exiting State": "Uscita stato",
    "Entering State (delayed)": "Ingresso stato (ritardato)",
    "Exiting State (delayed)": "Uscita stato (ritardato)",
    "Entering State (disable events)": "Ingresso stato (disabilita eventi)",
    "Entering State (re-enable events, delayed)": "Ingresso stato (riabilita eventi, ritardato)",
    "Entering State (delayed by state duration)": "Ingresso stato (ritardo = durata stato)",
    # ---- template UI strings ----
    "Latest Events": "Ultimi eventi",
    "Copy appliance name": "Copia nome dispositivo",
    # ---- appliance state labels (state.VALUE strings) ----
    "On": "Acceso",
    "Off": "Spento",
    "Fade In": "Accensione progressiva",
    "Fade Out": "Spegnimento progressivo",
    "Forced On": "Forzato acceso",
    "Forced Circadian Rhythm": "Ritmo circadiano forzato",
    "Circadian Rhythm": "Ritmo circadiano",
    "Opened": "Aperto",
    "Closed": "Chiuso",
    "Forced Opened": "Forzato aperto",
    "Forced Closed": "Forzato chiuso",
    "Lux Balance": "Bilanciamento lux",
    "none": "Nessuno",
    # ---- event type labels (LABEL constants) ----
    "Brightness": "Luminosità",
    "Hue": "Tonalità",
    "Saturation": "Saturazione",
    "Temperature": "Temperatura",
    "Duration": "Durata",
    "Cycles": "Cicli",
    "Period": "Periodo",
    "Show waveform?": "Forma d'onda?",
    "Starting brightness": "Luminosità iniziale",
    "Starting hue": "Tonalità iniziale",
    "Starting saturation": "Saturazione iniziale",
    "Ending brightness": "Luminosità finale",
    "Ending hue": "Tonalità finale",
    "Ending saturation": "Saturazione finale",
    "Sprinkling time duration": "Durata irrigazione",
    "Sprinkling time reduced duration": "Durata ridotta irrigazione",
    "Setpoint": "Setpoint",
    "Setpoint maintenance": "Manutenzione setpoint",
    "Is motion detected?": "È rilevato movimento?",
    "Is someone at home?": "C'è qualcuno in casa?",
    "Is coming someone?": "Sta arrivando qualcuno?",
    "Is it forced?": "È forzato?",
    "Toggling": "Alternanza",
    "User is": "L'utente è",
    "Scene is": "La scena è",
    "Wind is": "Il vento è",
    "Detach logic is": "Logica scollegata è",
    "Elapsed": "Trascorso",
    "Is it raining?": "Sta piovendo?",
    "Will it rain?": "Pioverà?",
    "Has it rained?": "Ha piovuto?",
    "Sun is": "Il sole è",
    "Sun brightness is": "La luminosità del sole è",
    "Is alarm armed?": "L'allarme è armato?",
    "Is alarm triggered?": "L'allarme è scattato?",
    "Season is": "La stagione è",
    "Command": "Comando",
    "Power consumption is": "Il consumo energetico è",
    "Power consumption": "Consumo energetico",
    "Power production is": "La produzione energetica è",
    "Power production": "Produzione energetica",
    "User": "Utente",
    "Volume": "Volume",
    "Playlist": "Playlist",
    "Sleepy Volume": "Volume addormentato",
    "Playlist user A": "Playlist utente A",
    "Playlist user B": "Playlist utente B",
    "Playlist user C": "Playlist utente C",
    "Christmas": "Natale",
    "Epiphany": "Epifania",
    "San Silvester": "San Silvestro",
    # ---- event descriptions (from get_description overrides) ----
    "Motion detected": "Movimento rilevato",
    "No motion": "Nessun movimento",
    "Someone is in home": "Qualcuno in casa",
    "No one is in home": "Nessuno in casa",
    "Is someone in here?": "C'è qualcuno qui?",
    "Someone is in here": "Qualcuno è qui",
    "No one is in here": "Nessuno qui",
    "Someone is coming": "Qualcuno sta arrivando",
    "No one is coming": "Nessuno sta arrivando",
    "Alarm is armed": "Allarme armato",
    "Alarm is not armed": "Allarme disarmato",
    "Alarm is triggered": "Allarme scattato",
    "Alarm is not triggered": "Allarme non attivo",
    "No rain": "Nessuna pioggia",
    "It is raining": "Sta piovendo",
    "Will rain": "Pioverà",
    "Will not rain": "Non pioverà",
    "Has rained": "Ha piovuto",
    "Has not rained": "Non ha piovuto",
    "Forced on": "Forzato acceso",
    "Forced off": "Forzato spento",
    "Unforced": "Non forzato",
    "Forced opened": "Forzato aperto",
    "Forced closed": "Forzato chiuso",
    "Forced circadian rhytm": "Ritmo circadiano forzato",
    "Forced lux balancing": "Bilanciamento lux forzato",
    "Forced show": "Spettacolo forzato",
    "Forced keeping": "Mantenimento forzato",
    "Partially On": "Parzialmente acceso",
    "Forced Partially On": "Parzialmente acceso forzato",
    # ---- composite enum descriptions (LABEL + _get_str, no override) ----
    "Elapsed yes": "Trascorso sì",
    "Elapsed no": "Trascorso no",
    "Detach logic is enabled": "Logica scollegata abilitata",
    "Detach logic is disabled": "Logica scollegata disabilitata",
    "Scene is playing": "Scena in riproduzione",
    "Scene is stopped": "Scena fermata",
    "User is asleep": "Utente addormentato",
    "User is awake": "Utente sveglio",
    "User is sleepy": "Utente assonnato",
    "Toggling enabled": "Alternanza abilitata",
    "Toggling disabled": "Alternanza disabilitata",
    "User A": "Utente A",
    "User B": "Utente B",
    "User C": "Utente C",
    "Wind is strong": "Vento forte",
    "Wind is weak": "Vento debole",
    "Sun is gone": "Sole tramontato",
    "Sun is over": "Sole alto",
    "Sun is rised": "Sole sorto",
    "Sun is set": "Sole tramontato",
    "Sun is rised (civil twilight)": "Sole sorto (crepuscolo civile)",
    "Sun is set (civil twilight)": "Sole tramontato (crepuscolo civile)",
    "Sun brightness is high": "Luminosità solare alta",
    "Sun brightness is low": "Luminosità solare bassa",
    "Sun brightness is very low": "Luminosità solare molto bassa",
    "Command on": "Comando acceso",
    "Command off": "Comando spento",
    "Command keep": "Comando mantenimento",
    "Season is winter": "Stagione invernale",
    "Season is summer": "Stagione estiva",
    "Season is sprint": "Stagione primaverile",
    "Season is fall": "Stagione autunnale",
    "Power consumption is off": "Consumo energetico assente",
    "Power consumption is low": "Consumo energetico basso",
    "Power consumption is high": "Consumo energetico alto",
    "Power consumption since short time": "Consumo energetico da poco",
    "Power consumption since long time": "Consumo energetico da molto",
    "Power production is off": "Produzione energetica assente",
    "Power production is low": "Produzione energetica bassa",
    "Power production is high": "Produzione energetica alta",
    "Power production since short time": "Produzione energetica da poco",
    "Power production since long time": "Produzione energetica da molto",
    # ---- _get_str values shown in event panels ----
    "yes": "sì",
    "asleep": "addormentato",
    "awake": "sveglio",
    "sleepy": "assonnato",
    "strong": "forte",
    "weak": "debole",
    "playing": "in riproduzione",
    "stopped": "fermato",
    "keep": "mantenimento",
    "winter": "inverno",
    "summer": "estate",
    "sprint": "primavera",
    "fall": "autunno",
    "high": "alta",
    "low": "bassa",
    "very low": "molto bassa",
    "gone": "tramontato",
    "over": "alto",
    "set": "tramontato",
    "rised": "sorto",
    "set (civil twilight)": "tramontato (crepuscolo civile)",
    "rised (civil twilight)": "sorto (crepuscolo civile)",
    "mist": "nebbia",
    "heavy raining": "pioggia intensa",
    "storm raining": "temporale",
    "since short time": "da poco",
    "since long time": "da molto",
    "day": "giorno",
    "eve": "vigilia",
    "time": "periodo",
    "is over": "terminato",
    "circadian rhythm": "ritmo circadiano",
    "lux balancing": "bilanciamento lux",
    "show": "spettacolo",
    "keeping": "mantenimento",
    # ---- enum value names from event_str.split('.')[-1] ----
    "Spotted": "Rilevato",
    "Missed": "Non rilevato",
    "Awake": "Sveglio",
    "Asleep": "Addormentato",
    "Sleepy": "Assonnato",
    "Strong": "Forte",
    "Weak": "Debole",
    "Triggered": "Attivato",
    "Untriggered": "Non attivato",
    "Sunleft": "Sole basso",
    "Bright": "Luminoso",
    "Dark": "Scuro",
    "DeepDark": "Molto scuro",
    "No": "No",
    "Mist": "Nebbia",
    "Gentle": "Leggera",
    "Heavy": "Intensa",
    "Storm": "Temporale",
    "Winter": "Inverno",
    "Summer": "Estate",
    "Spring": "Primavera",
    "Fall": "Autunno",
    "Not": "Non forzato",
    "PartiallyOn": "Parzialmente acceso",
    "CircadianRhythm": "Ritmo circadiano",
    "LuxBalance": "Bilanciamento lux",
    "Show": "Spettacolo",
    "Keep": "Mantenimento",
}

# ---------------------------------------------------------------------------
# Locale detection
# ---------------------------------------------------------------------------

_SUPPORTED = ("it", "en")


def get_locale(request) -> str:
    """Return the best supported locale from the Accept-Language header.

    Walks through tags in priority order (left to right) and returns the
    first match against the supported set {"it", "en"}.  Falls back to
    English when no supported tag is found.
    """
    header = request.headers.get("Accept-Language", "")
    for part in header.split(","):
        tag = part.strip().split(";")[0].strip().lower()
        if tag.startswith("it"):
            return "it"
        if tag.startswith("en"):
            return "en"
    return "en"


# ---------------------------------------------------------------------------
# Translator classes
# ---------------------------------------------------------------------------


class Translator:
    """Identity translator — returns every key unchanged (English pass-through)."""

    def __call__(self, key: str) -> str:
        return key


class LocaleTranslator(Translator):
    """Table-based translator that looks up *key* in *table*."""

    def __init__(self, table: dict) -> None:
        self._table = table

    def __call__(self, key: str) -> str:
        return self._table.get(key, key)


def make_translator(locale: str) -> Translator:
    """Return a :class:`Translator` for *locale*."""
    if locale == "it":
        return LocaleTranslator(_IT)
    return Translator()


# ---------------------------------------------------------------------------
# Translation (legacy function-based API used by templates via i18n_context)
# ---------------------------------------------------------------------------


def make_translate(locale: str):
    """Return a ``_(key) -> str`` callable for *locale*.

    Templates use ``{{ _("string") }}``; the returned object is a
    :class:`Translator` which is callable, so both usages are equivalent.
    """
    return make_translator(locale)


# ---------------------------------------------------------------------------
# Locale-aware timestamp formatting (no external dependency)
# ---------------------------------------------------------------------------

_MONTHS_IT = (
    "",
    "gen",
    "feb",
    "mar",
    "apr",
    "mag",
    "giu",
    "lug",
    "ago",
    "set",
    "ott",
    "nov",
    "dic",
)
_DAYS_IT = ("lun", "mar", "mer", "gio", "ven", "sab", "dom")


def make_format_ts(locale: str):
    """Return a ``format_ts(float) -> str`` callable for *locale*.

    English  →  ``time.ctime()`` style: "Mon Jan  6 14:32:01 2025"
    Italian  →  "lun 6 gen 2025 14:32:01"
    """
    if locale == "it":

        def format_ts(ts: float) -> str:
            try:
                dt = datetime.datetime.fromtimestamp(float(ts))
                d = _DAYS_IT[dt.weekday()]
                m = _MONTHS_IT[dt.month]
                return (
                    f"{d} {dt.day} {m} {dt.year} "
                    f"{dt.hour:02d}:{dt.minute:02d}:{dt.second:02d}"
                )
            except (OSError, ValueError, OverflowError):
                return ""

    else:

        def format_ts(ts: float) -> str:  # type: ignore[misc]
            try:
                return _time.ctime(float(ts))
            except (OSError, ValueError, OverflowError):
                return ""

    return format_ts


def make_format_ts_short(locale: str):
    """Shorter format used on the index page (today: HH:MM, other: d mon HH:MM)."""
    if locale == "it":

        def format_ts_short(
            dt: datetime.datetime, now: datetime.datetime
        ) -> str:
            if dt.date() == now.date():
                return dt.strftime("%H:%M")
            m = _MONTHS_IT[dt.month]
            return f"{dt.day} {m} {dt.strftime('%H:%M')}"

    else:

        def format_ts_short(  # type: ignore[misc]
            dt: datetime.datetime, now: datetime.datetime
        ) -> str:
            if dt.date() == now.date():
                return dt.strftime("%H:%M")
            return dt.strftime("%b %d %H:%M")

    return format_ts_short


# ---------------------------------------------------------------------------
# Context helper
# ---------------------------------------------------------------------------


def i18n_context(request) -> dict:
    """Return ``{'_': fn, 'format_ts': fn, 'locale': str}`` for *request*."""
    locale = get_locale(request)
    return {
        "_": make_translate(locale),
        "format_ts": make_format_ts(locale),
        "locale": locale,
    }
