import importlib

import pytest

from asserts.asserts import assert_true
from asserts.testcase import TestCase

solution = importlib.import_module('katas.8kyu.Grasshopper - summation.solution').summation

cases = [TestCase(1, 1), TestCase(8, 36), TestCase(22, 253), TestCase(100, 5050), TestCase(213, 22791)]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_grasshopper_summation(self, test):
        assert_true(solution(test.test_data), test.test_output)
