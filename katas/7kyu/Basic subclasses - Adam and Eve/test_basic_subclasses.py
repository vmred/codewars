import importlib

from asserts.asserts import assert_true

God = importlib.import_module('katas.7kyu.Basic subclasses - Adam and Eve.solution').God
Man = importlib.import_module('katas.7kyu.Basic subclasses - Adam and Eve.solution').Man


class TestSolution:
    def test_basic_subclasses(self):
        paradise = God()
        assert_true(isinstance(paradise[0], Man), True)
