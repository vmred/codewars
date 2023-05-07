import importlib
import pytest

from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.5kyu.String incrementer.solution').increment_string

cases = [
    Case("foo", "foo1"),
    Case("foobar001", "foobar002"),
    Case("foobar1", "foobar2"),
    Case("", "1"),
    Case("foobar99", "foobar100"),
    Case("foobar00", "foobar01"),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_string_incrementer(self, test):
        assert_true(solution(test.test_data), test.test_output)
