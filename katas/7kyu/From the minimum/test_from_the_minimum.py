import importlib
from asserts.asserts import assert_true

min_value = importlib.import_module('katas.7kyu.From the minimum.solution').min_value


class TestSolution:
    def test_from_the_minimum(self):
        assert_true(min_value([1, 3, 1]), 13)
        assert_true(min_value([4, 8, 1, 4]), 148)
