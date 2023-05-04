import importlib
import pytest

from asserts.asserts import assert_true
from asserts.testcase import TestCase

solution = importlib.import_module('katas.6kyu.com gov org first.solution').order_by_domain

cases = [
    TestCase(
        [
            "http://www.google.en/?x=jsdfkj",
            "http://www.google.de/?x=jsdfkj",
            "http://www.google.com/?x=jsdfkj",
            "http://www.google.org/?x=jsdfkj",
            "http://www.google.gov/?x=jsdfkj",
        ],
        [
            "http://www.google.com/?x=jsdfkj",
            "http://www.google.gov/?x=jsdfkj",
            "http://www.google.org/?x=jsdfkj",
            "http://www.google.de/?x=jsdfkj",
            "http://www.google.en/?x=jsdfkj",
        ],
    ),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_com_gov_org_first(self, test):
        assert_true(solution(test.test_data), test.test_output)
