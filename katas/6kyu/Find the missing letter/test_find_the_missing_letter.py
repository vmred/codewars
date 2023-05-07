import importlib
import pytest

from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.6kyu.Find the missing letter.solution').find_missing_letter

cases = [
    Case(['a', 'b', 'c', 'd', 'f'], 'e'),
    Case(['O', 'Q', 'R', 'S'], 'P'),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_find_the_missing_letter(self, test):
        assert_true(solution(test.test_data), test.test_output)
