# The following code was thought to be working properly,
# however when the code tries to access the age of the person instance it fails.

# person = Person('Yukihiro', 'Matsumoto', 47)
# print(person.full_name)
# print(person.age)


# class Person:
#     def __init__(self, first_name, last_name, age):
#         self.first_name = first_name
#         self.last_name = last_name
from asserts.Asserts import assert_true


class Person:
    def __init__(self, first_name, last_name, age):
        # self.first_name = first_name
        # self.last_name = last_name
        self.full_name = '{} {}'.format(first_name, last_name)
        self.age = age


matz = Person('Yukihiro', 'Matsumoto', 47)
assert_true(matz.full_name, 'Yukihiro Matsumoto')
assert_true(matz.age, 47)

joe = Person('Joe', 'Smith', 30)
assert_true(joe.full_name, 'Joe Smith')
assert_true(joe.age, 30)
