import re

from asserts.asserts import assert_true
import importlib

regex_contains_all = \
    importlib.import_module('kyu6.regex pattern to check if string has all characters.solution').regex_contains_all


class TestSolution:
    def test_regex_pattern_to_check_if_string_has_all_characters(self):
        pattern = regex_contains_all('abc')
        assert_true(bool(re.match(pattern, 'bca')), True)
        assert_true(bool(re.match(pattern, 'ac')), False)
