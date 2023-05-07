import importlib
import pytest

from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.6kyu.Word a10n (abbreviation).solution').abbreviate

cases = [
    Case("elephant-ride", "e6t-r2e"),
    Case('elephant-rides are really fun!', 'e6t-r3s are r4y fun!'),
    Case("sits'monolithic_on. a_sits, sits; on_cat; sat. ", "s2s'm8c_on. a_s2s, s2s; on_cat; sat. "),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_word_a10n_abbreviation(self, test):
        assert_true(solution(test.test_data), test.test_output)
