from asserts.asserts import assert_true
import importlib

is_prime = importlib.import_module('kyu6.Is a prime number.solution').is_prime


class TestSolution:
    def test_is_a_prime_number(self):
        assert_true(is_prime(75), False)
