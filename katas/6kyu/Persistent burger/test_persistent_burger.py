import importlib
from asserts.asserts import assert_true

persistence = importlib.import_module('katas.6kyu.Persistent burger.solution').persistence


class TestSolution:
    def test_persistent_burger(self):
        assert_true(persistence(39), 3)
