import importlib
import pytest
from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.3kyu.Last digit of a huge number.solution').last_digit

cases = [
    Case([], 1),
    # Case([0, 0], 1),
    Case([3, 4, 5], 1),
    Case([4, 3, 6], 4),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_last_digit_of_a_huge_number(self, test):
        assert_true(solution(test.test_data), test.test_output)
