from asserts.asserts import assert_true
import importlib

stock_list = importlib.import_module('katas.kyu6.Help the bookseller.solution').stock_list


class TestSolution:
    def test_help_the_bookseller(self):
        b = ["ABAR 200", "CDXE 500", "BKWR 250", "BTSQ 890", "DRTY 600"]
        c = ["A", "B"]
        assert_true(stock_list(b, c), "(A : 200) - (B : 1140)")
