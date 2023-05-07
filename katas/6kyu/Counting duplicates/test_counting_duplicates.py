import importlib

import pytest

from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.6kyu.Counting duplicates.solution').duplicate_count

cases = [
    Case("abcdea", 1),
    Case("abcdeaB", 2),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_counting_duplicates(self, test):
        assert_true(solution(test.test_data), test.test_output)
