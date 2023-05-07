import importlib
import pytest

from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.6kyu.Not prime numbers.solution').not_primes

cases = [
    Case([2, 222], [22, 25, 27, 32, 33, 35, 52, 55, 57, 72, 75, 77]),
    Case([2, 77], [22, 25, 27, 32, 33, 35, 52, 55, 57, 72, 75]),
    Case([2700, 3000], [2722, 2723, 2725, 2727, 2732, 2733, 2735, 2737, 2752, 2755, 2757, 2772, 2773, 2775]),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_not_prime_numbers(self, test):
        assert_true(solution(*test.test_data), test.test_output)
