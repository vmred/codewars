from asserts.asserts import assert_true
import importlib

sum_two_smallest_numbers = importlib.import_module(
    'kyu7.Sum of two lowest positive integers.solution').sum_two_smallest_numbers


class TestSolution:
    def test_sum_two_lowest_positive_integers(self):
        assert_true(sum_two_smallest_numbers([25, 42, 12, 18, 22]), 30)
        assert_true(sum_two_smallest_numbers([5, 8, 12, 18, 22]), 13)
