from asserts.Asserts import assert_true
import importlib

quicksort = importlib.import_module('kyu6.Bug Fix - Quick Sort.solution').quicksort


class TestSolution:
    def test_bug_fix_quick_sort(self):
        assert_true(quicksort([17, -5, 3]), [-5, 3, 17])
        assert_true(quicksort([3, 0, 7, 5, 1, 2, 9, 8, 4, 6]), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        assert_true(quicksort([]), [])
