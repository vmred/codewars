import importlib

dirReduc = importlib.import_module('kyu5.Directions reduction.solution').dirReduc


class TestSolution:

    def test_directions_reduction(self):
        a = dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"])
        e = ['WEST']
        assert (a == e), '--> actual: %s, expected %s' % (a, e)

        a = dirReduc(["NORTH", "WEST", "SOUTH", "EAST"])
        e = ["NORTH", "WEST", "SOUTH", "EAST"]
        assert (a == e), '--> actual: %s, expected %s' % (a, e)
