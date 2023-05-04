import importlib
from asserts.asserts import assert_true

special_number = importlib.import_module('katas.7kyu.Special number.solution').special_number


class TestSolution:
    def test_special_number(self):
        assert_true(special_number(2), 'Special!!')
        assert_true(special_number(39), "NOT!!")
        assert_true(special_number(11350224), 'Special!!')
