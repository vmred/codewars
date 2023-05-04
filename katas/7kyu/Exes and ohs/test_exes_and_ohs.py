import importlib
from asserts.asserts import assert_true

xo = importlib.import_module('katas.7kyu.Exes and ohs.solution').xo


class TestSolution:
    def test_exes_and_ohs(self):
        assert_true(xo('exes'), False)
        assert_true(xo('xoxo'), True)
        assert_true(xo(''), True)
