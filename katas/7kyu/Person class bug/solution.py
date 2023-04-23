# The following code was thought to be working properly,
# however when the code tries to access the age of the person instance it fails.

# person = Person('Yukihiro', 'Matsumoto', 47)
# print(person.full_name)
# print(person.age)


# class Person:
#     def __init__(self, first_name, last_name, age):
#         self.first_name = first_name
#         self.last_name = last_name


class Person:
    def __init__(self, first_name, last_name, age):
        # self.first_name = first_name
        # self.last_name = last_name
        self.full_name = '{} {}'.format(first_name, last_name)
        self.age = age
