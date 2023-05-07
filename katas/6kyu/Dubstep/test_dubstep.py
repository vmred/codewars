import importlib
import pytest

from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.6kyu.Dubstep.solution').song_decoder

cases = [Case("AWUBBWUBC", "A B C"), Case("AWUBWUBWUBBWUBWUBWUBC", "A B C")]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_dubstep(self, test):
        assert_true(solution(test.test_data), test.test_output)
