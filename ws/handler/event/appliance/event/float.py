from ws.handler.event.appliance.event.int import Handler as Parent


class Handler(Parent):
    def post(self, request_data):
        value = request_data["value"]
        event = self.KLASS(float(value))
        return event
