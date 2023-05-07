import importlib
import pytest

from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.6kyu.Find the unique number.solution').find_uniq

cases = [
    Case([1, 1, 1, 2, 1, 1], 2),
    Case([3, 4, 4, 4, 4, 4, 4, 4], 3),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_find_the_unique_number(self, test):
        assert_true(solution(test.test_data), test.test_output)
