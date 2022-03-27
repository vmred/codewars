from asserts.asserts import assert_true
import importlib

tower_builder = importlib.import_module('kyu6.Build the tower.solution').tower_builder


class TestSolution:
    def test_build_the_tower(self):
        assert_true(tower_builder(1), ['*', ])
        assert_true(tower_builder(3), ['  *  ', ' *** ', '*****'])
