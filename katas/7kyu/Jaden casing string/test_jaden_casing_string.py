import importlib
from asserts.asserts import assert_true

toJadenCase = importlib.import_module('katas.7kyu.Jaden casing string.solution').toJadenCase


class TestSolution:
    def test_jaden_casing_string(self):
        assert_true(
            toJadenCase('How can mirrors be real if our eyes aren\'t real'),
            'How Can Mirrors Be Real If Our Eyes Aren\'t Real',
        )
