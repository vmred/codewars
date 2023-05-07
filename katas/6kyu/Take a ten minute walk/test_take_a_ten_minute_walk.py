import importlib
import pytest

from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.6kyu.Take a ten minute walk.solution').isValidWalk

cases = [
    Case('nws', False),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_take_a_ten_minute_walk(self, test):
        assert_true(solution(test.test_data), test.test_output)
