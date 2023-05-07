import importlib
import pytest
from asserts.asserts import assert_true

from asserts.testcase import Case

solution = importlib.import_module('katas.7kyu.The @ operator.solution').evaluate

cases = [
    Case('0 @ 1', 0),
    Case('0 @ 2', 0),
    Case('1 @ 1', 4),
    Case('3 @ 2', 13),
    Case('6 @ 9', 66),
    Case('4 @ -4', -9),
    Case('1 @ 1 @ -4', -9),
    Case('2 @ 2 @ 2', 40),
    Case('0 @ 1 @ 2', 0),
    Case('5 @ 0', None),
]


class TestSolution:
    @pytest.mark.parametrize('tests', cases, ids=[f'{test.test_data}' for test in cases])
    def test_the_operator(self, tests):
        assert_true(solution(tests.test_data), tests.test_output)
