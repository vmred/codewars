import importlib
from asserts.asserts import assert_true

century = importlib.import_module('katas.7kyu.Century from year.solution').century


class TestSolution:
    def test_century_from_year(self):
        assert_true(century(1705), 18)
        assert_true(century(2000), 20)
