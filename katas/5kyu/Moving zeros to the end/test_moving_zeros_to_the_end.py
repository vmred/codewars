import importlib

import pytest

from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.5kyu.Moving zeros to the end.solution').move_zeros

cases = [
    Case([0, 1, None, 2, False, 1, 0], [1, None, 2, False, 1, 0, 0]),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_moving_zeros_to_the_end(self, test):
        assert_true(solution(test.test_data), test.test_output)
