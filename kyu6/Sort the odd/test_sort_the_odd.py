from asserts.Asserts import assert_true
import importlib

sort_array = importlib.import_module('kyu6.Sort the odd.solution').sort_array


class TestSolution:
    def test_sort_the_odd(self):
        assert_true(sort_array([5, 3, 2, 8, 1, 4]), [1, 3, 2, 8, 5, 4])
        assert_true(sort_array([5, 3, 1, 8, 0]), [1, 3, 5, 8, 0])
        assert_true(sort_array([]), [])
        assert_true(sort_array([1, 111, 11, 11, 2, 1, 5, 0]), [1, 1, 5, 11, 2, 11, 111, 0])
