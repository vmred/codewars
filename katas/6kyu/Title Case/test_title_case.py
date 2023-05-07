import importlib
import pytest

from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.6kyu.Title Case.solution').title_case

cases = [
    Case([''], ''),
    Case(['a clash of KINGS', 'a an the of'], 'A Clash of Kings'),
    Case(['THE WIND IN THE WILLOWS', 'The In'], 'The Wind in the Willows'),
    Case(['the quick brown fox'], 'The Quick Brown Fox'),
    Case(['a bc', 'bc'], 'A bc'),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_title_case(self, test):
        assert_true(solution(*test.test_data), test.test_output)
