mapper: dict = {}


def register_class(klass):
    if klass.KLASS is not None:
        mapper[klass.KLASS] = klass


class Registry(type):
    def __new__(mcs, name, bases, class_dict):
        cls = super().__new__(mcs, name, bases, class_dict)
        register_class(cls)
        return cls
