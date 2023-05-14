import importlib
import pytest
from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.5kyu.A Chain adding function.solution').add

cases = [
    Case(solution(1), 1),
    Case(solution(1)(2), 3),
    Case(solution(1)(2)(3), 6),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_a_chain_adding_function(self, test):
        assert_true(solution(test.test_data), test.test_output)
