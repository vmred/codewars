import importlib
import pytest

from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.6kyu.Bouncing Balls.solution').bouncingBall

cases = [
    Case([3, 0.66, 1.5], 3),
    Case([30, 0.66, 1.5], 15),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_bouncing_balls(self, test):
        assert_true(solution(*test.test_data), test.test_output)
