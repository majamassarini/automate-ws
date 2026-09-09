from typing import Optional

from ws.handler.scheduler.registry import Registry


class Handler(metaclass=Registry):
    KLASS = None
    KIND: Optional[str] = None

    def get_kind(self, trigger):
        if self.KIND:
            return self.KIND
        mod = type(trigger).__module__
        return ".".join(mod.split(".")[-2:]) if "." in mod else mod

    def get_details(self, trigger) -> list:
        """Return a list of {"label": str, "value": str} dicts."""
        return []
