from asserts.asserts import assert_true
import importlib

make_negative = importlib.import_module('katas.8kyu.Return negative.solution').make_negative


class TestSolution:
    def test_return_negative(self):
        assert_true(make_negative(42), -42)
