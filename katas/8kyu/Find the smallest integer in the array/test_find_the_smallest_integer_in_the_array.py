import importlib

import pytest

from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.8kyu.Find the smallest integer in the array.solution').find_smallest_int

cases = [
    Case([0, 1 - 2**64, 2**64], 1 - 2**64),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_find_the_smallest_in_the_array(self, test):
        assert_true(solution(test.test_data), test.test_output)
