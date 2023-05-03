import importlib

import pytest

from asserts.asserts import assert_true
from asserts.testcase import TestCase

solution = importlib.import_module('katas.5kyu.RGB To Hex Conversion.solution').rgb

cases = [
    TestCase([0, 0, 0], "000000"),
    TestCase([1, 2, 3], "010203"),
    TestCase([255, 255, 255], "FFFFFF"),
    TestCase([254, 253, 252], "FEFDFC"),
    TestCase([-20, 275, 125], "00FF7D"),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_rgb_to_hex_conversion(self, test):
        assert_true(solution(*test.test_data), test.test_output)
