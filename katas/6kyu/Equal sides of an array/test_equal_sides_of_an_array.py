import importlib

import pytest

from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.6kyu.Equal sides of an array.solution').find_even_index

cases = [
    Case([1, 2, 3, 4, 3, 2, 1], 3),
    Case([1, 2, 3, 4, 5, 6], -1),
    Case([20, 10, -80, 10, 10, 15, 35], 0),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_equal_sides_of_an_array(self, test):
        assert_true(solution(test.test_data), test.test_output)
