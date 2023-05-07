import importlib
import pytest

from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.6kyu.Pizza pieces.solution').max_pizza

cases = [Case(3, 7), Case(4, 11), Case(0, 1)]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_pizza_pieces(self, test):
        assert_true(solution(test.test_data), test.test_output)
