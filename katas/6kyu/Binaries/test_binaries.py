import importlib

import pytest

from asserts.asserts import assert_true
from asserts.testcase import Case

code = importlib.import_module('katas.6kyu.Binaries.solution').code
decode = importlib.import_module('katas.6kyu.Binaries.solution').decode

cases_code = [
    Case("62", "0011100110"),
    Case("55337700", "001101001101011101110011110011111010"),
    Case("69", "00111000011001"),
    Case("07", "10001111"),
    Case("1119441933000055", "1111110001100100110000110011000110010111011110101010001101001101"),
]

cases_decode = [
    Case("10001111", "07"),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases_code, ids=[f'{test.test_data}' for test in cases_code])
    def testing_code(self, test):
        assert_true(code(test.test_data), test.test_output)

    @pytest.mark.parametrize('test', cases_decode, ids=[f'{test.test_data}' for test in cases_decode])
    def testing_decode(self, test):
        assert_true(decode(test.test_data), test.test_output)
