from asserts.asserts import assert_true
import importlib

Primes = importlib.import_module('kyu5.First N prime numbers.solution').Primes


class TestSolution:

    def test_first_n_prime_numbers(self):
        assert_true(Primes.first(1), [2])
        assert_true(Primes.first(20)[-5:], [53, 59, 61, 67, 71])
