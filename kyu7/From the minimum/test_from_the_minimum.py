from asserts.Asserts import assert_true
import importlib

min_value = importlib.import_module('kyu7.From the minimum.solution').min_value


class TestSolution:
    def test_from_the_minimum(self):
        assert_true(min_value([1, 3, 1]), 13)
        assert_true(min_value([4, 8, 1, 4]), 148)
