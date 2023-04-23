import pytest

from asserts.asserts import assert_true
import importlib

decodeMorse = importlib.import_module('katas.6kyu.Decode the morse code.solution').decodeMorse


class TestSolution:
    @pytest.mark.not_completed
    @pytest.mark.xfail(reason='not completed')
    def test_decode_the_morse_code(self):
        assert_true(decodeMorse('.... . -.--   .--- ..- -.. .'), 'HEY JUDE')
        assert_true(decodeMorse('...---...'), 'SOS')
        assert_true(decodeMorse('  E E '), 'E E')
