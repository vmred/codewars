import importlib

import pytest

from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.4kyu.Human readable duration format.solution').format_duration

cases = [
    Case(1, '1 second'),
    Case(62, '1 minute and 2 seconds'),
    Case(120, '2 minutes'),
    Case(3600, '1 hour'),
    Case(3662, '1 hour, 1 minute and 2 seconds'),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_human_readable_duration_format(self, test):
        assert_true(solution(test.test_data), test.test_output)
