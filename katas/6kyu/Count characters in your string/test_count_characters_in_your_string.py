import importlib

import pytest

from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.6kyu.Count characters in your string.solution').count

cases = [
    Case("aba", {'a': 2, 'b': 1}),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_count_characters_in_your_string(self, test):
        assert_true(solution(test.test_data), test.test_output)
