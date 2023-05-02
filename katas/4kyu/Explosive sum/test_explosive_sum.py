import importlib

import pytest

from asserts.asserts import assert_true
from asserts.testcase import TestCase

solution = importlib.import_module('katas.4kyu.Explosive sum.solution').exp_sum

cases = [
    TestCase(1, 1),
    TestCase(2, 2),
    TestCase(3, 3),
    TestCase(4, 5),
    TestCase(5, 7),
    TestCase(10, 42),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_explosive_sum(self, test):
        assert_true(solution(test.test_data), test.test_output)
