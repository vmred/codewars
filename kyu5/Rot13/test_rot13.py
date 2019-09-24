import importlib

from asserts.Asserts import assert_true

rot13 = importlib.import_module('kyu5.Rot13.solution').rot13


class TestSolution:
    def test_rot13(self):
        assert_true(rot13("test"), "grfg")
        assert_true(rot13("Test"), "Grfg")
        assert_true(rot13('Pbqrjnef'), 'Codewars')
