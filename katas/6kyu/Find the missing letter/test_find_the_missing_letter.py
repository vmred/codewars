import importlib
from asserts.asserts import assert_true

find_missing_letter = importlib.import_module('katas.6kyu.Find the missing letter.solution').find_missing_letter


class TestSolution:
    def test_find_the_missing_letter(self):
        assert_true(find_missing_letter(['a', 'b', 'c', 'd', 'f']), 'e')
        assert_true(find_missing_letter(['O', 'Q', 'R', 'S']), 'P')
