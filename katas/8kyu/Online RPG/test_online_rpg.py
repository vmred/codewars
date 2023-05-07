import importlib

import pytest

from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.8kyu.Online RPG.solution').playerRankUp

cases = [
    Case(64, False),
    Case(180, 'Well done! You have advanced to the qualifying stage. Win 2 out of your next 3 games to rank up.'),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_online_rpg(self, test):
        assert_true(solution(test.test_data), test.test_output)
