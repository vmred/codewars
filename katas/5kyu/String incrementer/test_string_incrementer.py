import importlib

from asserts.asserts import assert_true

increment_string = importlib.import_module('katas.5kyu.String incrementer.solution').increment_string


class TestSolution:
    def test_string_incrementer(self):
        assert_true(increment_string("foo"), "foo1")
        assert_true(increment_string("foobar001"), "foobar002")
        assert_true(increment_string("foobar1"), "foobar2")
        assert_true(increment_string("foobar00"), "foobar01")
        assert_true(increment_string("foobar99"), "foobar100")
        assert_true(increment_string("foobar099"), "foobar100")
        assert_true(increment_string(""), "1")
