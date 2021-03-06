from asserts.Asserts import assert_true
import importlib

clean_string = importlib.import_module('kyu6.Backspaces in string.solution').clean_string


class TestSolution:
    def test_backspaces_in_string(self):
        assert_true(clean_string('abc#d##c'), 'ac')
        assert_true(clean_string('abc####d##c#'), '')
        assert_true(clean_string(""), '')
        assert_true(clean_string('w#h##E##b#9[z0,##'), '9[z')
