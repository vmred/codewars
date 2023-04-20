import importlib

from asserts.asserts import assert_true

rot13 = importlib.import_module('katas.kyu5.Rot13 kata.solution').rot13


class TestSolution:
    def test_rot13(self):
        assert_true(rot13("test"), "grfg")
        assert_true(rot13("Test"), "Grfg")
        assert_true(rot13('Pbqrjnef'), 'Codewars')
