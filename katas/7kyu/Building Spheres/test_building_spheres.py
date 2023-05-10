import importlib
import pytest
from asserts.asserts import assert_true
from asserts.testcase import Case

Sphere = importlib.import_module('katas.7kyu.Building Spheres.solution').Sphere

cases = [
    Case(Sphere(2, 50), 2, test_function='get_radius'),
    Case(Sphere(2, 50), 50, test_function='get_mass'),
    Case(Sphere(2, 50), 33.51032, test_function='get_volume'),
    Case(Sphere(2, 50), 50.26548, test_function='get_surface_area'),
    Case(Sphere(2, 50), 1.49208, test_function='get_density'),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_building_spheres(self, test):
        assert_true(getattr(test.test_data, test.test_function)(), test.test_output)
