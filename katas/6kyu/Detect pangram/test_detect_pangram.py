import importlib
import pytest

from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.6kyu.Detect pangram.solution').is_pangram

cases = [
    Case("The quick, brown fox jumps over the lazy dog!", True),
    Case('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa', False),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_pangram(self, test):
        assert_true(solution(test.test_data), test.test_output)
