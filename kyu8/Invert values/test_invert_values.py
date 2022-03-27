from asserts.asserts import assert_true
import importlib

invert = importlib.import_module('kyu8.Invert values.solution').invert


class TestSolution:
    def test_invert_values(self):
        assert_true(invert([1, 2, 3, 4, 5]), [-1, -2, -3, -4, -5])
        assert_true(invert([1, -2, 3, -4, 5]), [-1, 2, -3, 4, -5])
        assert_true(invert([]), [])
