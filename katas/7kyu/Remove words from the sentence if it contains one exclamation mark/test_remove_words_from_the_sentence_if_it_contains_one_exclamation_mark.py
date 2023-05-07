import importlib
import pytest

from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module(
    'katas.7kyu.Remove words from the sentence if it contains one exclamation mark.solution'
).remove

cases = [Case('Hi!', ''), Case('!!!Hi !!hi!!! !hi', '!!!Hi !!hi!!!'), Case('!Hi! ! !Hi!', '!Hi! !Hi!')]


class TestSolution:
    @pytest.mark.parametrize('tests', cases, ids=[f'{test.test_data}' for test in cases])
    def test_remove_words_from_the_sentence_if_it_contains_one_exclamation_mark(self, tests):
        assert_true(solution(tests.test_data), tests.test_output)
