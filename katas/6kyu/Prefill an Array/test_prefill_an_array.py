from asserts.asserts import assert_true
import importlib

prefill = importlib.import_module('katas.6kyu.Prefill an Array.solution').prefill


class TestSolution:
    def test_prefill_an_array(self):
        assert_true(prefill(3, 1), [1, 1, 1])
        assert_true(prefill(2, 'abc'), ['abc', 'abc'])
