from asserts.asserts import assert_true
import importlib

xo = importlib.import_module('katas.kyu7.Exes and ohs.solution').xo


class TestSolution:
    def test_exes_and_ohs(self):
        assert_true(xo('exes'), False)
        assert_true(xo('xoxo'), True)
        assert_true(xo(''), True)
