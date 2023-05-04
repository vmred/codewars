import importlib
from asserts.asserts import assert_true

get_sum = importlib.import_module('katas.7kyu.Beginner series #3 - Sum of numbers.solution').get_sum


class TestSolution:
    def test_sum_of_numbers(self):
        assert_true(get_sum(0, -1), -1)
        assert_true(get_sum(0, 1), 1)
