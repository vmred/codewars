import importlib
from asserts.asserts import assert_true

tribonacci = importlib.import_module('katas.6kyu.Tribonacci sequence.solution').tribonacci


class TestSolution:
    def test_tribonacci_sequence(self):
        assert_true(tribonacci([1, 1, 1], 10), [1, 1, 1, 3, 5, 9, 17, 31, 57, 105])
        assert_true(tribonacci([1, 1, 1], 1), [1])
