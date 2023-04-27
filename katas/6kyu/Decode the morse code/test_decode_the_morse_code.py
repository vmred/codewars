import pytest

from asserts.asserts import assert_true
import importlib

from asserts.testcase import TestCase

solution = importlib.import_module('katas.6kyu.Decode the morse code.solution').decodeMorse

cases = [
    TestCase('.... . -.--   .--- ..- -.. .', 'HEY JUDE'),
    TestCase('...---...', 'SOS'),
    TestCase('.   .', 'E E'),
    TestCase('----- .---- ..--- ---.. ----.', '01289')
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_decode_the_morse_code(self, test):
        assert_true(solution(test.test_data), test.test_output)
