from asserts.asserts import assert_true
import importlib

row_summ_odd_numbers = importlib.import_module('katas.kyu7.Sum of odd numbers.solution').row_summ_odd_numbers


class TestSolution:
    def test_sum_odd_numbers(self):
        assert_true(row_summ_odd_numbers(13), 2197)
        assert_true(row_summ_odd_numbers(2), 8)
