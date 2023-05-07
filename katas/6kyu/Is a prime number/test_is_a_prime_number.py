import importlib
import pytest

from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.6kyu.Is a prime number.solution').is_prime

cases = [Case(75, False), Case(1, False), Case(0, False), Case(-1, False), Case(2, True)]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_is_a_prime_number(self, test):
        assert_true(solution(test.test_data), test.test_output)
