import importlib
import pytest

from asserts.asserts import assert_true

from asserts.testcase import Case

solution = importlib.import_module(
    'katas.7kyu.Find the index of the second occurrence of a letter in a string.solution'
).second_symbol

cases = [Case(['Hello world!!!', 'l'], 3), Case(['', 'q'], -1)]


class TestSolution:
    @pytest.mark.parametrize('tests', cases, ids=[f'{test.test_data}' for test in cases])
    def test_find_the_index_of_the_second_occurrence_of_a_letter_in_a_string(self, tests):
        assert_true(solution(*tests.test_data), tests.test_output)
