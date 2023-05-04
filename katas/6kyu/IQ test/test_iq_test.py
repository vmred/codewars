import importlib
from asserts.asserts import assert_true

iq_test = importlib.import_module('katas.6kyu.IQ test.solution').iq_test


class TestSolution:
    def test_iq_test(self):
        assert_true(iq_test("2 4 7 8 10"), 3)
