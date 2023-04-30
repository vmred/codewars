import importlib

import pytest

from asserts.asserts import assert_true
from asserts.testcase import TestCase

solution = importlib.import_module('katas.8kyu.Find the nearest square number.solution').nearest_sq

cases = [
    TestCase(111, 121),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_find_the_nearest_square_number(self, test):
        assert_true(solution(test.test_data), test.test_output)
