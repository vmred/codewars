import importlib
import pytest

from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.6kyu.Simple string expansion.solution').string_expansion

cases = [
    Case('3abc', 'aaabbbccc'),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_simple_string_expansion(self, test):
        assert_true(solution(test.test_data), test.test_output)
