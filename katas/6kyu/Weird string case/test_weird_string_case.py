import importlib
import pytest

from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.6kyu.Weird string case.solution').to_weird_case

cases = [
    Case('This', 'ThIs'),
    Case('is', 'Is'),
    Case('This is a test', 'ThIs Is A TeSt'),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_weird_string_case(self, test):
        assert_true(solution(test.test_data), test.test_output)
