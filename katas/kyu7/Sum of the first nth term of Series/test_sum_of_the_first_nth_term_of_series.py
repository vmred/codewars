import importlib

from asserts.asserts import assert_true

series_sum = importlib.import_module('katas.kyu7.Sum of the first nth term of Series.solution').series_sum


class TestSolution:
    def test_sum_of_the_first_nth_term_of_series(self):
        assert_true(series_sum(1), "1.00")
        assert_true(series_sum(2), "1.25")
        assert_true(series_sum(3), "1.39")
