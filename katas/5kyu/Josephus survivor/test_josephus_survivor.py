import importlib

import pytest

from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.5kyu.Josephus survivor.solution').josephus_survivor

cases = [
    Case([7, 3], 4),
    Case([11, 19], 10),
    Case([1, 300], 1),
    Case([14, 2], 13),
    Case([100, 1], 100),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_josephus_survivor(self, test):
        assert_true(solution(*test.test_data), test.test_output)
