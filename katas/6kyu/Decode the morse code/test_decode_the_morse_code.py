import importlib
import pytest
from asserts.asserts import assert_true

from asserts.testcase import Case

solution = importlib.import_module('katas.6kyu.Decode the morse code.solution').decodeMorse

cases = [
    Case('.... . -.--   .--- ..- -.. .', 'HEY JUDE'),
    Case('...---...', 'SOS'),
    Case('.   .', 'E E'),
    Case('----- .---- ..--- ---.. ----.', '01289'),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_decode_the_morse_code(self, test):
        assert_true(solution(test.test_data), test.test_output)
