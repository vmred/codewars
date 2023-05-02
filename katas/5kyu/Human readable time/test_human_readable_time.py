import importlib

import pytest

from asserts.asserts import assert_true
from asserts.testcase import TestCase

solution = importlib.import_module('katas.5kyu.Human readable time.solution').make_readable

cases = [
    TestCase(0, "00:00:00"),
    TestCase(86399, "23:59:59"),
    TestCase(359999, "99:59:59"),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_human_readable_time(self, test):
        assert_true(solution(test.test_data), test.test_output)
