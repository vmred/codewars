import importlib

from asserts.asserts import assert_true

divisors = importlib.import_module('kyu7.Find the divisors!.solution').divisors


class TestSolution:
    def test_find_the_divisors(self):
        assert_true(divisors(15), [3, 5])
        assert_true(divisors(12), [2, 3, 4, 6])
        assert_true(divisors(13), "13 is prime")
