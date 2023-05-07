import importlib

import pytest

from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.6kyu.N smallest elements in original order.solution').first_n_smallest

cases = [
    Case([[1, 2, 3, 4, 5], 3], [1, 2, 3]),
    Case([[5, 4, 3, 2, 1], 3], [3, 2, 1]),
    Case([[1, 2, 3, 1, 2], 3], [1, 2, 1]),
    Case([[1, 2, 3, -4, 0], 3], [1, -4, 0]),
    Case([[1, 2, 3, 4, 5], 0], []),
    Case([[1, 2, 3, 4, 5], 5], [1, 2, 3, 4, 5]),
    Case([[1, 2, 3, 4, 2], 4], [1, 2, 3, 2]),
    Case([[2, 1, 2, 3, 4, 2], 2], [2, 1]),
    Case([[2, 1, 2, 3, 4, 2], 3], [2, 1, 2]),
    Case([[2, 1, 2, 3, 4, 2], 4], [2, 1, 2, 2]),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_n_smallest(self, test):
        assert_true(solution(*test.test_data), test.test_output)
