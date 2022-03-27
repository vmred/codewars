from asserts.asserts import assert_true
import importlib

nth_fib = importlib.import_module('kyu6.Nth Fibonacci.solution').nth_fib


class TestSolution:
    def test_nth_fibonacci(self):
        assert_true(nth_fib(1), 0)
        assert_true(nth_fib(13), 144)
        assert_true(nth_fib(2), 1)
