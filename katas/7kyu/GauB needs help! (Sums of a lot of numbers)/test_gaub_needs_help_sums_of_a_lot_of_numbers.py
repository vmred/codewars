import importlib
from asserts.asserts import assert_true

f = importlib.import_module('katas.7kyu.GauB needs help! (Sums of a lot of numbers).solution').f


class TestSolution:
    def test_gaub_needs_help_sums_of_a_lot_of_numbers(self):
        assert_true(f(1), 1)
        assert_true(f(100), 5050)
