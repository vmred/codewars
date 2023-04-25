import importlib

from asserts.asserts import assert_true

rot13 = importlib.import_module('katas.5kyu.Rot13.solution').rot13


class TestSolution:
    def test_rot13(self):
        assert_true(rot13("test"), "grfg")
        assert_true(rot13("Test"), "Grfg")
        assert_true(rot13('Pbqrjnef'), 'Codewars')
