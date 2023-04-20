from asserts.asserts import assert_true
import importlib

countBits = importlib.import_module('katas.kyu6.Bit counting.solution').countBits


class TestSolution:
    def test_bit_counting(self):
        assert_true(countBits(10), 2)
        assert_true(countBits(1234), 5)
