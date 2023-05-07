import importlib
import pytest

from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.6kyu.Multiples of 3 and 5.solution').solution

cases = [
    Case(10, 23),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_multiples_of_3_and_5(self, test):
        assert_true(solution(test.test_data), test.test_output)
