import importlib

import pytest

from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.6kyu.Thinkful Logic Drills - Red and bumpy.solution').color_probability

cases = [
    Case(['red', 'bumpy'], '0.57'),
    Case(['green', 'bumpy'], '0.14'),
    Case(['yellow', 'smooth'], '0.33'),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_thinkful_logic_drills_red_and_bumpy(self, test):
        assert_true(solution(*test.test_data), test.test_output)
