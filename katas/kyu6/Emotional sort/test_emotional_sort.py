import pytest
from asserts.asserts import assert_true
import importlib
from asserts.testcase import TestCase

solution = importlib.import_module('katas.kyu6.Emotional sort.solution').sort_emotions

cases = [
    TestCase([[':D', 'T_T', ':D', ':('], True], [':D', ':D', ':(', 'T_T']),
    TestCase([['T_T', ':D', ':(', ':('], True], [':D', ':(', ':(', 'T_T']),
    TestCase([[':)', 'T_T', ':)', ':D', ':D'], True], [':D', ':D', ':)', ':)', 'T_T']),
    TestCase([[':D', 'T_T', ':D', ':('], False], ['T_T', ':(', ':D', ':D']),
    TestCase([[], False], []),
    TestCase([[], True], []),
]


class TestSolution:

    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_emotional_sort(self, test):
        assert_true(solution(*test.test_data), test.test_output)
