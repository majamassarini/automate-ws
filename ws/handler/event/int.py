from ws.handler.event import handler


class Bean(handler.Bean):
    def __init__(self, label, module, klass, template, icon, value):
        super(Bean, self).__init__(label, module, klass, template, icon)
        self.value = value


class Handler(handler.Handler):

    KLASS = int
    TEMPLATE = "event/int.html"
    LABEL = "Value: "

    def get(self, event):
        return Bean(
            self.LABEL,
            self.get_module_str(),
            self.get_class_str(),
            self.TEMPLATE,
            self.get_icon(event),
            event,
        )

    def post(self, request_data):
        value = request_data["value"]
        event = self.KLASS(value)
        return event

    def get_description(self, event):
        return "{} {}".format(event, self.LABEL)

    def get_description_for_index(self, event):
        return ""

    def get_icon(self, event):
        return ""
