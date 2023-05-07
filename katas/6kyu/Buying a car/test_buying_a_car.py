import importlib
import pytest

from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.6kyu.Buying a car.solution').nbMonths

cases = [
    Case([2000, 8000, 1000, 1.5], [6, 766]),
    Case([12000, 8000, 1000, 1.5], [0, 4000]),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_buying_a_car(self, test):
        assert_true(solution(*test.test_data), test.test_output)
