from asserts.asserts import assert_true
import importlib

first_non_consecutive = importlib.import_module('katas.kyu8.First non-consecutive number.solution').first_non_consecutive


class TestSolution:
    def test_first_nonconsecutive_number(self):
        assert_true(first_non_consecutive([1, 2, 3, 4, 6, 7, 8]), 6)
        assert_true(first_non_consecutive([1, 2, 3, 4, 5, 6, 7, 8]), None)
        assert_true(first_non_consecutive([4, 6, 7, 8, 9, 11]), 6)
        assert_true(first_non_consecutive([4, 5, 6, 7, 8, 9, 11]), 11)
        assert_true(first_non_consecutive([31, 32]), None)
        assert_true(first_non_consecutive([-3, -2, 0, 1]), 0)
        assert_true(first_non_consecutive([-5, -4, -3, -1]), -1)
