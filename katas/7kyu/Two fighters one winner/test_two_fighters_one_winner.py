import importlib
from asserts.asserts import assert_true

declare_winner = importlib.import_module('katas.7kyu.Two fighters one winner.solution').declare_winner
Fighter = importlib.import_module('katas.7kyu.Two fighters one winner.solution').Fighter


class TestSolution:
    def test_two_fighters_one_winner(self):
        assert_true(declare_winner(Fighter("Lew", 10, 2), Fighter("Harry", 5, 4), "Lew"), "Lew")
