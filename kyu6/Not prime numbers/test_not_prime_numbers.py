from asserts.asserts import assert_true
import importlib

not_primes = importlib.import_module('kyu6.Not prime numbers.solution').not_primes


class TestSolution:
    def test_not_prime_numbers(self):
        assert_true(not_primes(2, 222), [22, 25, 27, 32, 33, 35, 52, 55, 57, 72, 75, 77])
        assert_true(not_primes(2, 77), [22, 25, 27, 32, 33, 35, 52, 55, 57, 72, 75])
        assert_true(not_primes(2700, 3000),
                    [2722, 2723, 2725, 2727, 2732, 2733, 2735, 2737, 2752, 2755, 2757, 2772, 2773, 2775])
