# Classy Classes
# Basic Classes, this kata is mainly aimed at the new JS ES6 Update introducing classes
# Task
# Your task is to complete this Class, the Person class has been created. 
# You must fill in the Constructor method to accept a name as string and an age as number, 
# complete the get Info property and getInfo method/Info getter which should return
# johns age is 34
from asserts.asserts import assert_true


class Person:
    def __init__(self, name, age):
        self.info = f'{name}s age is {age}'


person = Person('Alex', 16)
assert_true(person.info, 'Alexs age is 16')
