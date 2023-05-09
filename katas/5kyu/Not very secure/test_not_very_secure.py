import importlib
import pytest
from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.5kyu.Not very secure.solution').alphanumeric

cases = [
    Case("hello world_", False),
    Case("PassW0rd", True),
    Case("", False),
    Case("     ", False),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_not_very_secure(self, test):
        assert_true(solution(test.test_data), test.test_output)
