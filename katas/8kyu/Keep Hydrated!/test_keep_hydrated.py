import importlib

import pytest

from asserts.asserts import assert_true
from asserts.testcase import TestCase

solution = importlib.import_module('katas.8kyu.Keep Hydrated!.solution').litres

cases = [
    TestCase(2, 1),
    TestCase(1.4, 0),
    TestCase(12.3, 6),
    TestCase(0.82, 0),
    TestCase(11.8, 5),
    TestCase(1787, 893),
    TestCase(0, 0),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_keep_hydrated(self, test):
        assert_true(solution(test.test_data), test.test_output)
