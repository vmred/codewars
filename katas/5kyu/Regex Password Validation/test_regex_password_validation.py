import importlib
from re import search

import pytest

from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.5kyu.Regex Password Validation.solution').regex

cases = [
    Case('fjd3IR9', True),
    Case('ghdfj32', False),
    Case('DSJKHD23', False),
    Case('dsF43', False),
    Case('4fdg5Fj3', True),
    Case('fjd3IR9.;', False),
    Case('DHSJdhjsU', False),
    Case('fjd3  IR9', False),
    Case('djI38D55', True),
    Case('a2.d412', False),
    Case('jfkdfj3j', False),
    Case('Password123', True),
    Case('123abcABC', True),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_regex_password_validation(self, test):
        assert_true(bool(search(solution, test.test_data)), test.test_output)
