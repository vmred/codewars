import importlib
import pytest

from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.6kyu.Two Joggers.solution').nbr_of_laps

cases = [
    Case([5, 3], (3, 5)),
    Case([4, 6], (3, 2)),
    Case([5, 5], (1, 1)),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_two_joggers(self, test):
        assert_true(solution(*test.test_data), test.test_output)
