from asserts.asserts import assert_true
import importlib

Person = importlib.import_module('katas.kyu8.Classy Classes.solution').Person


class TestSolution:
    def test_classy_classes(self):
        person = Person('Alex', 16)
        assert_true(person.info, 'Alexs age is 16')
