import importlib
import pytest

from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.6kyu.Two Sum.solution').two_sum

cases = [
    Case([[1, 2, 3], 4], [0, 2]),
    Case([[1234, 5678, 9012], 14690], [1, 2]),
    Case([[2, 2, 3], 4], [0, 1]),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_two_sum(self, test):
        assert_true(solution(*test.test_data), test.test_output)
