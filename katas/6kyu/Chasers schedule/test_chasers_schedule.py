import importlib
import pytest
from asserts.asserts import assert_true

from asserts.testcase import TestCase

solution = importlib.import_module('katas.6kyu.Chasers schedule.solution').solution

cases = [TestCase([2, 4], 10), TestCase([4, 3], 17), TestCase([810, 410], 435420)]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_chasers_schedule(self, test):
        assert_true(solution(*test.test_data), test.test_output)
