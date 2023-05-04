def class_name_changer(cls, new_name):
    if not new_name.isalnum() or not new_name[0].isupper():
        raise ValueError

    cls.__name__ = new_name


class MyClass:
    def __str__(self):
        return str(type(self))
