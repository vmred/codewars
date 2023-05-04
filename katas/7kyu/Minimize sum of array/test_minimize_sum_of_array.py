import importlib
from asserts.asserts import assert_true

min_sum = importlib.import_module('katas.7kyu.Minimize sum of array.solution').min_sum


class TestSolution:
    def test_minimize_sum_of_array(self):
        assert_true(min_sum([5, 4, 2, 3]), 22)
        assert_true(min_sum([9, 2, 8, 7, 5, 4, 0, 6]), 74)
