import pytest

from asserts.asserts import assert_true
import importlib

from utils.utils import Test

solution = importlib.import_module('kyu7.The @ operator.solution').evaluate

tests = [
    Test('0 @ 1', 0),
    Test('0 @ 2', 0),
    Test('1 @ 1', 4),
    Test('3 @ 2', 13),
    Test('6 @ 9', 66),
    Test('4 @ -4', -9),
    Test('1 @ 1 @ -4', -9),
    Test('2 @ 2 @ 2', 40),
    Test('0 @ 1 @ 2', 0),
    Test('5 @ 0', None),
]


class TestSolution:
    @pytest.mark.parametrize('tests', tests, ids=[test.test_data for test in tests])
    def test_the_operator(self, tests):
        assert_true(solution(tests.test_data), tests.test_output)
