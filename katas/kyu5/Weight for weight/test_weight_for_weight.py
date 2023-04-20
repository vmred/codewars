import importlib

from asserts.asserts import assert_true

order_weight = importlib.import_module('katas.kyu5.Weight for weight.solution').order_weight


class TestSolution:
    def test_weight_for_weight(self):
        # assert_true(order_weight("103 123 4444 99 2000"), "2000 103 123 4444 99")
        assert_true(order_weight("2000 10003 1234000 44444444 9999 11 11 22 123"),
                    "11 11 2000 10003 22 123 1234000 44444444 9999")
