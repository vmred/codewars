import importlib
import pytest
from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.6kyu.Array diff.solution').array_diff

cases = [
    Case([[1, 2], [1]], [2]),
    Case([[1, 2, 2], []], [1, 2, 2]),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_array_diff(self, test):
        assert_true(solution(*test.test_data), test.test_output)
