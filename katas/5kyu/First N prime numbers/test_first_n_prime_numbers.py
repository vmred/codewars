import importlib
import pytest
from asserts.asserts import assert_true

from asserts.testcase import Case

Primes = importlib.import_module('katas.5kyu.First N prime numbers.solution').Primes

cases = [
    Case(1, [2]),
    # Case(20, [53, 59, 61, 67, 71]),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_first_n_prime_numbers(self, test):
        assert_true(Primes.first(test.test_data), test.test_output)
