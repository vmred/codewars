from asserts.asserts import assert_true
import importlib

nbr_of_laps = importlib.import_module('kyu6.Two Joggers.solution').nbr_of_laps


class TestSolution:
    def test_two_joggers(self):
        assert_true(nbr_of_laps(5, 3), (3, 5))
        assert_true(nbr_of_laps(4, 6), (3, 2))
        assert_true(nbr_of_laps(5, 5), (1, 1))
