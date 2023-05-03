import importlib
from re import search

import pytest

from asserts.asserts import assert_true
from asserts.testcase import TestCase

solution = importlib.import_module('katas.5kyu.Regex Password Validation.solution').regex

cases = [
    TestCase('fjd3IR9', True),
    TestCase('ghdfj32', False),
    TestCase('DSJKHD23', False),
    TestCase('dsF43', False),
    TestCase('4fdg5Fj3', True),
    TestCase('fjd3IR9.;', False),
    TestCase('DHSJdhjsU', False),
    TestCase('fjd3  IR9', False),
    TestCase('djI38D55', True),
    TestCase('a2.d412', False),
    TestCase('jfkdfj3j', False),
    TestCase('Password123', True),
    TestCase('123abcABC', True),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_regex_password_validation(self, test):
        assert_true(bool(search(solution, test.test_data)), test.test_output)
