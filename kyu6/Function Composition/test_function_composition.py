from asserts.Asserts import assert_true
import importlib

compose = importlib.import_module('kyu6.Function Composition.solution').compose


class TestSolution:
    def test_function_composition(self):
        assert_true(compose(lambda a: a + 1, lambda a: a)(0), 1)
