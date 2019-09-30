from asserts.Asserts import assert_true
import importlib

century = importlib.import_module('kyu7.Century from year.solution').century


class TestSolution:
    def test_century_from_year(self):
        assert_true(century(1705), 18)
        assert_true(century(2000), 20)
