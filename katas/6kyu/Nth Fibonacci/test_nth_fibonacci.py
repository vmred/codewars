import importlib
import pytest

from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.6kyu.Nth Fibonacci.solution').nth_fib

cases = [Case(1, 0), Case(13, 144), Case(2, 1)]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_nth_fibonacci(self, test):
        assert_true(solution(test.test_data), test.test_output)
