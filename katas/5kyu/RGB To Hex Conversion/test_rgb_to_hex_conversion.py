import importlib

import pytest

from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.5kyu.RGB To Hex Conversion.solution').rgb

cases = [
    Case([0, 0, 0], "000000"),
    Case([1, 2, 3], "010203"),
    Case([255, 255, 255], "FFFFFF"),
    Case([254, 253, 252], "FEFDFC"),
    Case([-20, 275, 125], "00FF7D"),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_rgb_to_hex_conversion(self, test):
        assert_true(solution(*test.test_data), test.test_output)
