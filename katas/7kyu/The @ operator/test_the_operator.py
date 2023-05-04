import importlib
import pytest
from asserts.asserts import assert_true

from asserts.testcase import TestCase

solution = importlib.import_module('katas.7kyu.The @ operator.solution').evaluate

cases = [
    TestCase('0 @ 1', 0),
    TestCase('0 @ 2', 0),
    TestCase('1 @ 1', 4),
    TestCase('3 @ 2', 13),
    TestCase('6 @ 9', 66),
    TestCase('4 @ -4', -9),
    TestCase('1 @ 1 @ -4', -9),
    TestCase('2 @ 2 @ 2', 40),
    TestCase('0 @ 1 @ 2', 0),
    TestCase('5 @ 0', None),
]


class TestSolution:
    @pytest.mark.parametrize('tests', cases, ids=[f'{test.test_data}' for test in cases])
    def test_the_operator(self, tests):
        assert_true(solution(tests.test_data), tests.test_output)
