from asserts.asserts import assert_true
import importlib

has_subpattern = importlib.import_module('katas.6kyu.String subpattern recognition I.solution').has_subpattern


class TestSolution:
    def test_string_subpattern_recognition_i(self):
        assert_true(has_subpattern("a"), False)
        assert_true(has_subpattern("aaaa"), True)
        assert_true(has_subpattern("abcd"), False)
        assert_true(has_subpattern("abababab"), True)
        assert_true(has_subpattern("ababababa"), False)
        assert_true(has_subpattern("123a123a123a"), True)
        assert_true(has_subpattern("123A123a123a"), False)
        assert_true(has_subpattern("abbaabbaabba"), True)
        assert_true(has_subpattern("abbabbabba"), False)
        assert_true(has_subpattern("abcdabcabcd"), False)
