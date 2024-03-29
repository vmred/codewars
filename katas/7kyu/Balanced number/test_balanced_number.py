import importlib
from asserts.asserts import assert_true

balanced_num = importlib.import_module('katas.7kyu.Balanced number.solution').balanced_num


class TestSolution:
    def test_balanced_number(self):
        assert_true(balanced_num(7), "Balanced")
        assert_true(balanced_num(959), "Balanced")
        assert_true(balanced_num(13), "Balanced")
        assert_true(balanced_num(432), "Not Balanced")
        assert_true(balanced_num(424), "Balanced")
        assert_true(balanced_num(56239814), 'Balanced')
