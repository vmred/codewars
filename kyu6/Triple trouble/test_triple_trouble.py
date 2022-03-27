from asserts.asserts import assert_true
import importlib

triple_double = importlib.import_module('kyu6.Triple trouble.solution').triple_double


class TestSolution:
    def test_triple_trouble(self):
        assert_true(triple_double(451999277, 41177722899), 1)
        assert_true(triple_double(1112, 122), 0)
        assert_true(triple_double(10560002, 100), 1)
