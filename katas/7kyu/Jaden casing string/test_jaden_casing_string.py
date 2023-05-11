import importlib
from asserts.asserts import assert_true

to_jaden_case = importlib.import_module('katas.7kyu.Jaden casing string.solution').to_jaden_case


class TestSolution:
    def test_jaden_casing_string(self):
        assert_true(
            to_jaden_case('How can mirrors be real if our eyes aren\'t real'),
            'How Can Mirrors Be Real If Our Eyes Aren\'t Real',
        )
