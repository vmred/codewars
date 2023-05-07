import importlib

import pytest

from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.8kyu.Keep Hydrated!.solution').litres

cases = [
    Case(2, 1),
    Case(1.4, 0),
    Case(12.3, 6),
    Case(0.82, 0),
    Case(11.8, 5),
    Case(1787, 893),
    Case(0, 0),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_keep_hydrated(self, test):
        assert_true(solution(test.test_data), test.test_output)
