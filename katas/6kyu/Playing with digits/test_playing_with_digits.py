import importlib
import pytest

from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.6kyu.Playing with digits.solution').dig_pow

cases = [
    Case([46288, 3], 51),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_playing_with_digits(self, test):
        assert_true(solution(*test.test_data), test.test_output)
