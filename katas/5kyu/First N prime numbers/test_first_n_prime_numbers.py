import importlib
import pytest
from asserts.asserts import assert_true

from asserts.testcase import TestCase

Primes = importlib.import_module('katas.5kyu.First N prime numbers.solution').Primes

cases = [
    TestCase(1, [2]),
    # TestCase(20, [53, 59, 61, 67, 71]),  # TODO
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_first_n_prime_numbers(self, test):
        assert_true(Primes.first(test.test_data), test.test_output)
