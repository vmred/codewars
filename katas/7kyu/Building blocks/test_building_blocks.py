import importlib
import pytest
from asserts.asserts import assert_true
from asserts.testcase import Case

Block = importlib.import_module('katas.7kyu.Building blocks.solution').Block

cases = [
    Case(Block([2, 2, 2]), 2, test_function='get_width'),
    Case(Block([2, 2, 2]), 2, test_function='get_length'),
    Case(Block([2, 2, 2]), 2, test_function='get_height'),
    Case(Block([2, 2, 2]), 8, test_function='get_volume'),
    Case(Block([2, 2, 2]), 24, test_function='get_surface_area'),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_building_blocks(self, test):
        assert_true(getattr(test.test_data, test.test_function)(), test.test_output)
