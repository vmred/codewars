import importlib
import pytest

from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.6kyu.Number Zoo Patrol.solution').find_missing_number

cases = [Case([2, 3, 4], 1), Case([1, 2, 3], 4), Case([1, 2, 4], 3)]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_find_missing_number(self, test):
        assert_true(solution(test.test_data), test.test_output)
