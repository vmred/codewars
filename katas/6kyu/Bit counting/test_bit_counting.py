from asserts.asserts import assert_true
import importlib

countBits = importlib.import_module('katas.6kyu.Bit counting.solution').countBits


class TestSolution:
    def test_bit_counting(self):
        assert_true(countBits(10), 2)
        assert_true(countBits(1234), 5)
