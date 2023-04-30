import importlib

import pytest

from asserts.asserts import assert_true
from asserts.testcase import TestCase

solution = importlib.import_module('katas.8kyu.Count sheep.solution').count_sheeps

cases = [
    TestCase(
        [
            True,
            True,
            True,
            False,
            True,
            True,
            True,
            True,
            True,
            False,
            True,
            False,
            True,
            False,
            False,
            True,
            True,
            True,
            True,
            True,
            False,
            False,
            True,
            True,
        ],
        17,
    ),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_count_sheep(self, test):
        assert_true(solution(test.test_data), test.test_output)
