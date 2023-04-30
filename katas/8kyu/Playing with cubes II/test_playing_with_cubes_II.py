import importlib
import pytest

from asserts.asserts import assert_true

from asserts.testcase import TestCase

Cube = importlib.import_module('katas.8kyu.Playing with cubes II.solution').Cube

cases = [TestCase(10, 10), TestCase('no args', 0)]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_playing_with_cubes_2(self, test):
        cube = test.test_data != 'no args' and Cube(test.test_data) or Cube()
        assert_true(cube.get_side(), test.test_output)
