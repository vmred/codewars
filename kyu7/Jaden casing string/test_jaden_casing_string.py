from asserts.Asserts import assert_true
import importlib

toJadenCase = importlib.import_module('kyu7.Jaden casing string.solution').toJadenCase


class TestSolution:
    def test_jaden_casing_string(self):
        assert_true(toJadenCase('How can mirrors be real if our eyes aren\'t real'),
                    'How Can Mirrors Be Real If Our Eyes Aren\'t Real')
