import importlib
import pytest

from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.6kyu.Emotional sort.solution').sort_emotions

cases = [
    Case([[':D', 'T_T', ':D', ':('], True], [':D', ':D', ':(', 'T_T']),
    Case([['T_T', ':D', ':(', ':('], True], [':D', ':(', ':(', 'T_T']),
    Case([[':)', 'T_T', ':)', ':D', ':D'], True], [':D', ':D', ':)', ':)', 'T_T']),
    Case([[':D', 'T_T', ':D', ':('], False], ['T_T', ':(', ':D', ':D']),
    Case([[], False], []),
    Case([[], True], []),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_emotional_sort(self, test):
        assert_true(solution(*test.test_data), test.test_output)
