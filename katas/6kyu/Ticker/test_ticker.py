import importlib
import pytest

from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.6kyu.Ticker.solution').ticker

cases = [
    Case(['Beautiful is better than ugly.', 10, 0], '          '),
    Case(['Beautiful is better than ugly.', 10, 1], '         B'),
    Case(['Beautiful is better than ugly.', 10, 30], 'than ugly.'),
    Case(['such now time be?', 1, 4651], 'o'),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_ticker(self, test):
        assert_true(solution(*test.test_data), test.test_output)
