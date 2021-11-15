from ws.handler.event.int import Handler as Parent, Bean


class Handler(Parent):
    def get(self, event):
        return Bean(
            self.LABEL,
            self.get_module_str(),
            self.get_class_str(),
            self.TEMPLATE,
            self.get_icon(event),
            event.value,
        )

    def post(self, request_data):
        value = request_data["value"]
        event = self.KLASS(int(value))
        return event

    def get_icon(self, event):
        return None
