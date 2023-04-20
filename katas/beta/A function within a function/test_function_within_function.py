import importlib

from asserts.asserts import assert_true

always = importlib.import_module('katas.beta.A function within a function.solution').always


class TestSolution:
    def test_function_within_function(self):
        three = always(3)
        assert_true(three(), 3)
