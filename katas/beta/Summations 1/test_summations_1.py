import importlib

from asserts.asserts import assert_true

summation = importlib.import_module('katas.beta.Summations 1.solution').summation


class TestSolution:
    def test_summation_1(self):
        assert_true(summation(0), 0)
        assert_true(summation(1), 1)
        assert_true(summation(25), 325)
        assert_true(summation(10), 55)
        assert_true(summation(5), 15)
        assert_true(summation("538"), "Invalid Value")
        assert_true(summation(67.9), "Invalid Value")
