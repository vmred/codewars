from asserts.Asserts import assert_true
import importlib

xo = importlib.import_module('kyu7.Exes and ohs.solution').xo


class TestSolution:
    def test_exes_and_ohs(self):
        assert_true(xo('exes'), False)
        assert_true(xo('xoxo'), True)
        assert_true(xo(''), True)
