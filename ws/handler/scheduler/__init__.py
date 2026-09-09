from ws.handler.scheduler import registry
from ws.handler.scheduler.handler import Handler

for _module in (
    "sun",
    "cron",
    "interval",
    "state",
    "circadian_rhythm",
    "date",
    "crawler",
    "protocol",
):
    try:
        __import__(f"ws.handler.scheduler.{_module}")
    except ImportError:
        pass
