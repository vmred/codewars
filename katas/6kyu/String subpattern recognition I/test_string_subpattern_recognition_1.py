import importlib
import pytest

from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.6kyu.String subpattern recognition I.solution').has_subpattern

cases = [
    Case('a', False),
    Case('aaaa', True),
    Case('abcd', False),
    Case('abababab', True),
    Case('123a123a123a', True),
    Case('abcdabcabcd', False),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_string_subpattern_recognition_i(self, test):
        assert_true(solution(test.test_data), test.test_output)
