from asserts.Asserts import assert_true
import importlib

row_weights = importlib.import_module('kyu7.Row weights.solution').row_weights


class TestSolution:
    def test_row_weights(self):
        assert_true(row_weights([80]), (80, 0))
        assert_true(row_weights([50, 60, 70, 80]), (120, 140))
