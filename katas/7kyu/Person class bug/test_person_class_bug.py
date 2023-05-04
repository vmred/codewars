import importlib
from asserts.asserts import assert_true

Person = importlib.import_module('katas.7kyu.Person class bug.solution').Person


class TestSolution:
    def test_person_class_bug(self):
        matz = Person('Yukihiro', 'Matsumoto', 47)
        assert_true(matz.full_name, 'Yukihiro Matsumoto')
        assert_true(matz.age, 47)

        joe = Person('Joe', 'Smith', 30)
        assert_true(joe.full_name, 'Joe Smith')
        assert_true(joe.age, 30)
