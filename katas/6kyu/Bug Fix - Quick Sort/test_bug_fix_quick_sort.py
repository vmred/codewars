import importlib
import pytest

from asserts.asserts import assert_true
from asserts.testcase import TestCase

solution = importlib.import_module('katas.6kyu.Bug Fix - Quick Sort.solution').quicksort

cases = [
    TestCase([17, -5, 3], [-5, 3, 17]),
    TestCase([3, 0, 7, 5, 1, 2, 9, 8, 4, 6], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]),
    TestCase([], []),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_bug_fix_quick_sort(self, test):
        assert_true(solution(test.test_data), test.test_output)
