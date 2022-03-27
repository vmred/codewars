import importlib

from asserts.asserts import assert_true

flatten = importlib.import_module('beta.Flattening Lists.solution').flatten


class TestSolution:
    def test_flattening_lists(self):
        assert_true(flatten([[1, 2], [3, 4]]), [1, 2, 3, 4])
        assert_true(flatten([[1], [2], [3], [4]]), [1, 2, 3, 4])
