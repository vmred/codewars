import importlib

from asserts.asserts import assert_true

factorial = importlib.import_module('kyu7.Factorial kata.solution').factorial


class TestSolution:
    def test_factorial(self):
        assert_true(factorial(0), 1)
        assert_true(factorial(1), 1)
        assert_true(factorial(2), 2)
        assert_true(factorial(3), 6)
