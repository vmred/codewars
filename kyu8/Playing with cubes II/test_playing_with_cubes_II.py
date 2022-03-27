from asserts.asserts import assert_true
import importlib

Cube = importlib.import_module('kyu8.Playing with cubes II.solution').Cube


class TestSolution:
    def test_playing_with_cubes_2(self):
        c = Cube(10)
        assert_true(c.get_side(), 10)
        c = Cube()
        assert_true(c.get_side(), 0)
