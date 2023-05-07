import importlib
import pytest

from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.6kyu.Unique in order.solution').unique_in_order

cases = [
    Case('AAAABBBCCDAABBB', ['A', 'B', 'C', 'D', 'A', 'B']),
    Case([1, 2, 2, 3, 3], [1, 2, 3]),
    Case('A', ['A']),
    Case('AA', ['A']),
    Case('', []),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_unique_in_order(self, test):
        assert_true(solution(test.test_data), test.test_output)
