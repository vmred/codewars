import importlib
import pytest

from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.6kyu.Your orders please.solution').order

cases = [
    Case('is2 Thi1s T4est 3a', 'Thi1s is2 3a T4est'),
    Case('4of Fo1r pe6ople g3ood th5e the2', 'Fo1r the2 g3ood 4of th5e pe6ople'),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_your_orders_please(self, test):
        assert_true(solution(test.test_data), test.test_output)
