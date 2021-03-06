from asserts.Asserts import assert_true
import importlib

two_sum = importlib.import_module('kyu6.Two Sum.solution').two_sum


class TestSolution:
    def test_two_sum(self):
        assert_true(sorted(two_sum([1, 2, 3], 4)), [0, 2])
        assert_true(sorted(two_sum([1234, 5678, 9012], 14690)), [1, 2])
        assert_true(sorted(two_sum([2, 2, 3], 4)), [0, 1])
