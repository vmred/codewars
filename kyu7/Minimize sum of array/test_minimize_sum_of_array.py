from asserts.Asserts import assert_true
import importlib

min_sum = importlib.import_module('kyu7.Minimize sum of array.solution').min_sum


class TestSolution:
    def test_minimize_sum_of_array(self):
        assert_true(min_sum([5, 4, 2, 3]), 22)
        assert_true(min_sum([9, 2, 8, 7, 5, 4, 0, 6]), 74)
