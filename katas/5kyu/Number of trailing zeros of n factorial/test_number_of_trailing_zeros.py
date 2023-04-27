from asserts.asserts import assert_true
import importlib

zeros = importlib.import_module('katas.5kyu.Number of trailing zeros of n factorial.solution').zeros


class TestSolution:
    def test_numer_of_trailing_zeros_of_n_factorial(self):
        assert_true(zeros(0), 0)
        assert_true(zeros(6), 1)
        assert_true(zeros(30), 7)
