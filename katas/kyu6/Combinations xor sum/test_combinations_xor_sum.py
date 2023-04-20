from asserts.asserts import assert_true
import importlib

transform = importlib.import_module('katas.kyu6.Combinations xor sum.solution').transform


class TestSolution:
    def test_combinations_xor_sum(self):
        assert_true(transform([7, 4, 11, 6, 5], 3), 384)
        assert_true(transform([12, 9, 16, 11, 10], 4), 7937)
        assert_true(transform([9, 6, 13, 9, 7], 2), 375)
