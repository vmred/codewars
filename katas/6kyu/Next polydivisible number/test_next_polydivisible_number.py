import importlib

import pytest

from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.6kyu.Next polydivisible number.solution').next_num

cases = [
    Case(0, 1),
    Case(10, 12),
    Case(11, 12),
    Case(1234, 1236),
    Case(123220, 123252),
    Case(1234567890, 1236004020),
    Case(8375699373040516261617982, None),
    Case(3608528850368400786036725, None),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_next_polydivisible_number(self, test):
        assert_true(solution(test.test_data), test.test_output)
