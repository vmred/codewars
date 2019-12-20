from asserts.Asserts import assert_true
import importlib

f = importlib.import_module('kyu7.GauB needs help! (Sums of a lot of numbers).solution').f


class TestSolution:
    def test_gaub_needs_help_sums_of_a_lot_of_numbers(self):
        assert_true(f(1), 1)
        assert_true(f(100), 5050)
