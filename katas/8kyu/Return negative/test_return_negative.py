import importlib

import pytest

from asserts.asserts import assert_true
from asserts.testcase import TestCase

solution = importlib.import_module('katas.8kyu.Return negative.solution').make_negative

cases = [
    TestCase(42, -42),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_return_negative(self, test):
        assert_true(solution(test.test_data), test.test_output)
