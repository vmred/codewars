from asserts.asserts import assert_true
import importlib

next_happy_year = importlib.import_module('katas.kyu7.See your next happy year.solution').next_happy_year


class TestSolution:
    def test_see_your_next_happy_year(self):
        assert_true(next_happy_year(1001), 1023)
