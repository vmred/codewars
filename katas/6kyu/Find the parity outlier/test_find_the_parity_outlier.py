import importlib

import pytest

from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.6kyu.Find the parity outlier.solution').find_outlier

cases = [
    Case([2, 4, 0, 100, 4, 11, 2602, 36], 11),
    Case([160, 3, 1719, 19, 11, 13, -21], 160),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_find_the_parity_outlier(self, test):
        assert_true(solution(test.test_data), test.test_output)
