import importlib

import pytest

from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.6kyu.Count letters in string.solution').letter_count

cases = [
    Case("codewars", {"a": 1, "c": 1, "d": 1, "e": 1, "o": 1, "r": 1, "s": 1, "w": 1}),
    Case("activity", {"a": 1, "c": 1, "i": 2, "t": 2, "v": 1, "y": 1}),
    Case('arithmetics', {"a": 1, "c": 1, "e": 1, "h": 1, "i": 2, "m": 1, "r": 1, "s": 1, "t": 2}),
    Case('traveller', {"a": 1, "e": 2, "l": 2, "r": 2, "t": 1, "v": 1}),
    Case('daydreamer', {"a": 2, "d": 2, "e": 2, "m": 1, "r": 2, "y": 1}),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_count_letters_in_string(self, test):
        assert_true(solution(test.test_data), test.test_output)
