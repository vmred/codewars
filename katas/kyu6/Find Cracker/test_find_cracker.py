import pytest
from asserts.asserts import assert_true
import importlib
from asserts.testcase import TestCase

solution = importlib.import_module('katas.kyu6.Find Cracker.solution').find_hack

tests = [
    TestCase([
        ["name1", 150, ["B", "A", "A", "C", "A", "A"]],
        ["name2", 120, ["B", "A", "A", "A"]],
        ["name3", 160, ["B", "A", "A", "A", "A"]],
        ["name4", 140, ["B", "A", "A", "C", "A"]]
    ], ['name2', 'name4'])
]


class TestSolution:
    @pytest.mark.parametrize('tests', tests, ids=[f'{test.test_data}' for test in tests])
    def test_find_cracker(self, tests):
        assert_true(solution(tests.test_data), tests.test_output)
