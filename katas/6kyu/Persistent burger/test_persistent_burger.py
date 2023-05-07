import importlib
import pytest

from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.6kyu.Persistent burger.solution').persistence

cases = [Case(39, 3), Case(1, 0), Case(0, 0), Case(543, 2)]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_persistent_burger(self, test):
        assert_true(solution(test.test_data), test.test_output)
