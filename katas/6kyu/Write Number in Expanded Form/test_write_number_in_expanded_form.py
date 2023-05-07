import importlib
import pytest

from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.6kyu.Write Number in Expanded Form.solution').expanded_form

cases = [
    Case(12, '10 + 2'),
    Case(42, '40 + 2'),
    Case(70304, '70000 + 300 + 4'),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_write_number_in_expanded_form(self, test):
        assert_true(solution(test.test_data), test.test_output)
