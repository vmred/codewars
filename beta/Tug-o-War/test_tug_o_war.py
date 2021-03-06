import importlib

from asserts.Asserts import assert_true

tug_o_war = importlib.import_module('beta.Tug-o-War.solution').tug_o_war


class TestSolution:
    def test_tug_o_war(self):
        assert_true(tug_o_war([[1, 2, 3, 4, 6], [5, 4, 3, 2, 1]]), "Team 1 wins!")
