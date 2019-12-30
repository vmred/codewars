from asserts.Asserts import assert_true
import importlib

quicksort = importlib.import_module('kyu6.Bug Fix - Quick Sort.solution').quicksort


class TestSolution:
    def test_bug_fix_quick_sort(self):
        assert_true(quicksort([17, -5, 3]), [-5, 3, 17])
