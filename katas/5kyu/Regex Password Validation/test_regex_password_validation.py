import importlib
from re import search

from asserts.asserts import assert_true

regex = importlib.import_module('katas.5kyu.Regex Password Validation.solution').regex


class TestSolution:
    def test_regex_password_validation(self):
        assert_true(bool(search(regex, 'fjd3IR9')), True)
        assert_true(bool(search(regex, 'ghdfj32')), False)
        assert_true(bool(search(regex, 'DSJKHD23')), False)
        assert_true(bool(search(regex, 'dsF43')), False)
        assert_true(bool(search(regex, '4fdg5Fj3')), True)
        assert_true(bool(search(regex, 'DHSJdhjsU')), False)
        assert_true(bool(search(regex, 'fjd3IR9.;')), False)
        assert_true(bool(search(regex, 'fjd3  IR9')), False)
        assert_true(bool(search(regex, 'djI38D55')), True)
        assert_true(bool(search(regex, 'a2.d412')), False)
        assert_true(bool(search(regex, 'JHD5FJ53')), False)
        assert_true(bool(search(regex, '!fdjn345')), False)
        assert_true(bool(search(regex, 'jfkdfj3j')), False)
        assert_true(bool(search(regex, '123')), False)
        assert_true(bool(search(regex, 'abc')), False)
        assert_true(bool(search(regex, '123abcABC')), True)
        assert_true(bool(search(regex, 'ABC123abc')), True)
        assert_true(bool(search(regex, 'Password123')), True)
