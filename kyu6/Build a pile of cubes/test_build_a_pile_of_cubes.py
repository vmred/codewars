from asserts.asserts import assert_true
import importlib

find_nb = importlib.import_module('kyu6.Build a pile of cubes.solution').find_nb


class TestSolution:
    def test_build_a_pile_of_cubes(self):
        assert_true(find_nb(4183059834009), 2022)
        assert_true(find_nb(24723578342962), -1)
