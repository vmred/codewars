import importlib
import pytest

from asserts.asserts import assert_true

from asserts.testcase import Case

solution = importlib.import_module('katas.5kyu.Greed is good.solution').score

cases = [
    Case([2, 3, 4, 6, 2], 0),
    Case([4, 4, 4, 3, 3], 400),
    Case([2, 4, 4, 5, 4], 450),
    Case([1, 1, 1, 1], 1100),
    Case([1, 1, 1, 1], 1100),
    Case([1, 1, 1, 3, 3], 1000),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_greed_is_good(self, test):
        assert_true(solution(test.test_data), test.test_output)
