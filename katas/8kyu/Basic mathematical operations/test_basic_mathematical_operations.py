import importlib

import pytest

from asserts.asserts import assert_true
from asserts.testcase import TestCase

solution = importlib.import_module('katas.8kyu.Basic mathematical operations.solution').basic_op

cases = [
    TestCase(['+', 4, 7], 11),
    TestCase(['-', 15, 18], -3),
    TestCase(['*', 5, 5], 25),
    TestCase(['/', 49, 7], 7),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_basic_mathematical_operations(self, test):
        assert_true(solution(*test.test_data), test.test_output)
