import importlib
import pytest

from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.6kyu.What century is it.solution').whatCentury

cases = [
    Case('1999', '20th'),
    Case('2000', '20th'),
    Case('1322', '14th'),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_what_century_is_it(self, test):
        assert_true(solution(test.test_data), test.test_output)
