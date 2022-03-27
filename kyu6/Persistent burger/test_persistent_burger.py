from asserts.asserts import assert_true
import importlib

persistence = importlib.import_module('kyu6.Persistent burger.solution').persistence


class TestSolution:
    def test_persistent_burger(self):
        assert_true(persistence(39), 3)
