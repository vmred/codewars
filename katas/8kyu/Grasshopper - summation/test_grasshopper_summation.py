import importlib

import pytest

from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.8kyu.Grasshopper - summation.solution').summation

cases = [Case(1, 1), Case(8, 36), Case(22, 253), Case(100, 5050), Case(213, 22791)]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_grasshopper_summation(self, test):
        assert_true(solution(test.test_data), test.test_output)
