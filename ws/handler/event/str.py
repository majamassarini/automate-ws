from ws.handler.event.int import handler


class Handler(handler.Handler):

    KLASS = str
    TEMPLATE = "event/str.html"
