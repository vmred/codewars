import importlib
import pytest

from asserts.asserts import assert_true

from asserts.testcase import Case

solution = importlib.import_module('katas.6kyu.Binary to text ASCII conversion.solution').binary_to_string

cases = [
    Case('0100100001100101011011000110110001101111', 'Hello'),
    Case('00110001001100000011000100110001', '1011'),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_binary_to_text_ascii_conversion(self, test):
        assert_true(solution(test.test_data), test.test_output)
