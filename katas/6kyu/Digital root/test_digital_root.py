from asserts.asserts import assert_true
import importlib

digital_root = importlib.import_module('katas.6kyu.Digital root.solution').digital_root


class TestSolution:
    def test_digital_root(self):
        assert_true(digital_root(456), 6)
