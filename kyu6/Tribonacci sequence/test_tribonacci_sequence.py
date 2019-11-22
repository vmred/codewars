from asserts.Asserts import assert_true
import importlib

tribonacci = importlib.import_module('kyu6.Tribonacci sequence.solution').tribonacci


class TestSolution:
    def test_tribonacci_sequence(self):
        assert_true(tribonacci([1, 1, 1], 10), [1, 1, 1, 3, 5, 9, 17, 31, 57, 105])
        assert_true(tribonacci([1, 1, 1], 1), [1])
