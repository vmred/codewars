from asserts.asserts import assert_true
import importlib

pig_it = importlib.import_module('katas.5kyu.Simple pig latin.solution').pig_it


class TestSolution:

    def test_simple_pig_latin(self):
        assert_true(pig_it('Pig latin is cool'), 'igPay atinlay siay oolcay')
        assert_true(pig_it('This is my string'), 'hisTay siay ymay tringsay')
        assert_true(pig_it('Quis custodiet ipsos custodes ?'), 'uisQay ustodietcay psosiay ustodescay ?')
