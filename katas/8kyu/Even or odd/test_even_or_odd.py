from asserts.asserts import assert_true
import importlib

even_or_odd = importlib.import_module('katas.8kyu.Even or odd.solution').even_or_odd


class TestSolution:
    def test_even_or_odd(self):
        assert_true(even_or_odd(2), "Even")
