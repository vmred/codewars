import pytest

from asserts.asserts import assert_true
import importlib

from asserts.testcase import TestCase

solution = importlib.import_module(
    'katas.7kyu.Find the index of the second occurrence of a letter in a string.solution').second_symbol

tests = [
    TestCase(['Hello world!!!', 'l'], 3),
    TestCase(['', 'q'], -1)
]


class TestSolution:
    @pytest.mark.parametrize('tests', tests, ids=[f'{test.test_data}' for test in tests])
    def test_find_the_index_of_the_second_occurrence_of_a_letter_in_a_string(self, tests):
        assert_true(solution(*tests.test_data), tests.test_output)
