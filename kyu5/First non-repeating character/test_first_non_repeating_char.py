import importlib

from asserts.asserts import assert_true

first_non_repeating_letter = importlib.import_module(
    'kyu5.First non-repeating character.solution').first_non_repeating_letter


class TestSolution:
    def test_first_non_repeating_char(self):
        assert_true(first_non_repeating_letter('a'), 'a')
        assert_true(first_non_repeating_letter('stress'), 't')
        assert_true(first_non_repeating_letter('moonmen'), 'e')

        assert_true(first_non_repeating_letter(''), '')
        assert_true(first_non_repeating_letter('hello world, eh?'), 'w')

        assert_true(first_non_repeating_letter('sTreSS'), 'T')
