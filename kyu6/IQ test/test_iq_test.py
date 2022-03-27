from asserts.asserts import assert_true
import importlib

iq_test = importlib.import_module('kyu6.IQ test.solution').iq_test


class TestSolution:
    def test_iq_test(self):
        assert_true(iq_test("2 4 7 8 10"), 3)
