import importlib

import pytest

from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.6kyu.Replace with alphabet position.solution').alphabet_position

cases = [
    Case('The narwhal bacons at midnight.', '20 8 5 14 1 18 23 8 1 12 2 1 3 15 14 19 1 20 13 9 4 14 9 7 8 20'),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_replace_with_alphabet_position(self, test):
        assert_true(solution(test.test_data), test.test_output)
