import importlib
import pytest

from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.6kyu.Mexican wave.solution').wave

cases = [
    Case('hello', ["Hello", "hEllo", "heLlo", "helLo", "hellO"]),
    Case('codewars', ["Codewars", "cOdewars", "coDewars", "codEwars", "codeWars", "codewArs", "codewaRs", "codewarS"]),
    Case(' gap ', [" Gap ", " gAp ", " gaP "]),
    Case('', []),
    Case('two words', ["Two words", "tWo words", "twO words", "two Words", "two wOrds", "two woRds", "two worDs", "two wordS"]),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_mexican_wave(self, test):
        assert_true(solution(test.test_data), test.test_output)
