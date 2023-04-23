from asserts.asserts import assert_true
import importlib

sum_arrays = importlib.import_module('katas.6kyu.Sum two arrays.solution').sum_arrays


class TestSolution:
    def test_sum_two_arrays(self):
        assert_true(sum_arrays([], []), [])
        assert_true(sum_arrays([3, 2, 9], [1, 2]), [3, 4, 1])
        assert_true(sum_arrays([-3, 4, 2], [3, 4, 4]), [2])
        assert_true(sum_arrays([0], []), [0])
        assert_true(sum_arrays([-4, 9, 3, 1, 0], [2, 4]), [-4, 9, 2, 8, 6])
