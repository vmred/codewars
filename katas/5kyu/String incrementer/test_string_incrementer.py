import importlib
import pytest

from asserts.asserts import assert_true
from asserts.testcase import TestCase

solution = importlib.import_module('katas.5kyu.String incrementer.solution').increment_string

cases = [
    TestCase("foo", "foo1"),
    TestCase("foobar001", "foobar002"),
    TestCase("foobar1", "foobar2"),
    TestCase("", "1"),
    TestCase("foobar99", "foobar100"),
    TestCase("foobar00", "foobar01"),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_string_incrementer(self, test):
        assert_true(solution(test.test_data), test.test_output)
