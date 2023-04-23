import importlib

from asserts.asserts import assert_true

solution = importlib.import_module('katas.5kyu.First non-repeating character.solution').first_non_repeating_letter


class TestSolution:
    def test_first_non_repeating_char(self):
        assert_true(solution('a'), 'a')
        assert_true(solution('stress'), 't')
        assert_true(solution('moonmen'), 'e')
        assert_true(solution(''), '')
        assert_true(solution('hello world, eh?'), 'w')
        assert_true(solution('sTreSS'), 'T')
