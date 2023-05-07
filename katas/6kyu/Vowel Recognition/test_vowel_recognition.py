import importlib
import pytest

from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.6kyu.Vowel Recognition.solution').vowel_recognition

cases = [
    Case('baceb', 16),
    Case('aeiouAEIOU', 220),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_vowel_recognition(self, test):
        assert_true(solution(test.test_data), test.test_output)
