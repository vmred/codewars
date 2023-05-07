import importlib
import re
import pytest

from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module(
    'katas.6kyu.regex pattern to check if string has all characters.solution'
).regex_contains_all

cases = [
    Case(['abc', 'bca'], True),
    Case(['abc', 'ac'], False),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_regex_pattern_to_check_if_string_has_all_characters(self, test):
        pattern = solution(test.test_data[0])
        assert_true(bool(re.match(pattern, test.test_data[1])), test.test_output)
