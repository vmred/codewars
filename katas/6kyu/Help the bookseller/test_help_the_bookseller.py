import importlib

import pytest

from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.6kyu.Help the bookseller.solution').stock_list

cases = [
    Case([["ABAR 200", "CDXE 500", "BKWR 250", "BTSQ 890", "DRTY 600"], ["A", "B"]], "(A : 200) - (B : 1140)"),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_help_the_bookseller(self, test):
        assert_true(solution(*test.test_data), test.test_output)
