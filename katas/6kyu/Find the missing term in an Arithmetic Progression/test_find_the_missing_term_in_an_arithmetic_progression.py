import importlib

import pytest

from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module(
    'katas.6kyu.Find the missing term in an Arithmetic Progression.solution'
).find_missing

cases = [
    Case([1, 2, 3, 4, 6, 7, 8, 9], 5),
    Case([1, 3, 4, 5, 6, 7, 8, 9], 2),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_find_the_missing_term_in_an_arithmetic_progression(self, test):
        assert_true(solution(test.test_data), test.test_output)
