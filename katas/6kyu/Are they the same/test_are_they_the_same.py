import importlib
import pytest

from asserts.asserts import assert_true

from asserts.testcase import TestCase

solution = importlib.import_module('katas.6kyu.Are they the same.solution').comp

cases = [
    TestCase([[121, 144, 19, 161, 19, 144, 19, 11], [121, 14641, 20736, 361, 25921, 361, 20736, 361]], True),
    TestCase([[10, 99], [101, 9801]], False),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_explosive_sum(self, test):
        assert_true(solution(*test.test_data), test.test_output)
