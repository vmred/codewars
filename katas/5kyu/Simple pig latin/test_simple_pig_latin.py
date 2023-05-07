import importlib

import pytest

from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.5kyu.Simple pig latin.solution').pig_it

cases = [
    Case('Pig latin is cool', 'igPay atinlay siay oolcay'),
    Case('This is my string', 'hisTay siay ymay tringsay'),
    Case('Quis custodiet ipsos custodes ?', 'uisQay ustodietcay psosiay ustodescay ?'),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_simple_pig_latin(self, test):
        assert_true(solution(test.test_data), test.test_output)
