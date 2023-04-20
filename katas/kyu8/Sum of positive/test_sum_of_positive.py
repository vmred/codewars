from asserts.asserts import assert_true
import importlib

positive_sum = importlib.import_module('katas.kyu8.Sum of positive.solution').positive_sum


class TestSolution:
    def test_sum_of_positive(self):
        assert_true(positive_sum([-1, 2, 3, 4, -5]), 9)
