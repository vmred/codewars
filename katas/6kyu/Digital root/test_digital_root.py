import importlib
import pytest

from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.6kyu.Digital root.solution').digital_root

cases = [
    Case(456, 6),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_digital_root(self, test):
        assert_true(solution(test.test_data), test.test_output)
