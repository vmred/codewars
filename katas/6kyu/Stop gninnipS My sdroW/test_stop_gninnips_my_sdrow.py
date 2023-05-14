import importlib
import pytest
from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.6kyu.Stop gninnipS My sdroW.solution').spin_words

cases = [
    Case('Welcome', 'emocleW'),
    Case('to', 'to'),
    Case('CodeWars', 'sraWedoC'),
    Case('Hey fellow warriors', 'Hey wollef sroirraw'),
]


class TestSolution:

    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_stop_gninnips_my_sdrow(self, test):
        assert_true(solution(test.test_data), test.test_output)
