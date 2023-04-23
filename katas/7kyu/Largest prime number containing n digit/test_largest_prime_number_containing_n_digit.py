from asserts.asserts import assert_true
import importlib

largest = importlib.import_module('katas.7kyu.Largest prime number containing n digit.solution').largest


class TestSolution:
    def test_largest_prime_number_containing_n_digit(self):
        assert_true(largest(2), 97)
