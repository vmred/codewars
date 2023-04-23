from asserts.asserts import assert_true
import importlib

remove_char = importlib.import_module('katas.8kyu.Remove first and last character.solution').remove_char


class TestSolution:
    def test_remove_first_and_last_character(self):
        assert_true(remove_char('eloquent'), 'loquen')
        assert_true(remove_char('ok'), '')
