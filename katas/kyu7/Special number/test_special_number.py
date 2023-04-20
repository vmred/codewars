from asserts.asserts import assert_true
import importlib

special_number = importlib.import_module('katas.kyu7.Special number.solution').special_number


class TestSolution:
    def test_special_number(self):
        assert_true(special_number(2), 'Special!!')
        assert_true(special_number(39), "NOT!!")
        assert_true(special_number(11350224), 'Special!!')
