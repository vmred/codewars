import importlib

import pytest

from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.8kyu.Basic mathematical operations.solution').basic_op

cases = [
    Case(['+', 4, 7], 11),
    Case(['-', 15, 18], -3),
    Case(['*', 5, 5], 25),
    Case(['/', 49, 7], 7),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_basic_mathematical_operations(self, test):
        assert_true(solution(*test.test_data), test.test_output)
