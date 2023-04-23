import importlib

from asserts.asserts import assert_true

valid_parentheses = importlib.import_module('katas.5kyu.Valid Parentheses.solution').valid_parentheses


class TestSolution:
    def test_valid_parentheses(self):
        assert_true(valid_parentheses("  ("), False, "should work for '  ('")
        assert_true(valid_parentheses(")test"), False, "should work for ')test'")
        assert_true(valid_parentheses(""), True, "should work for ''")
        assert_true(valid_parentheses("hi())("), False, "should work for 'hi())('")
        assert_true(valid_parentheses("hi(hi)()"), True, "should work for 'hi(hi)()'")
