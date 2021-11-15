from ws.handler import appliance_mapper as mapper


def register_class(klass):
    mapper[klass.KLASS] = klass


class Registry(type):
    def __new__(mcs, name, bases, class_dict):
        cls = super().__new__(mcs, name, bases, class_dict)
        register_class(cls)
        return cls
