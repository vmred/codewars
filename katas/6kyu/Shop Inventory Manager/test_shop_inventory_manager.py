import importlib
import pytest

from asserts.asserts import assert_true
from asserts.testcase import Case

items = importlib.import_module('katas.6kyu.Shop Inventory Manager.solution').items
update_quality = importlib.import_module('katas.6kyu.Shop Inventory Manager.solution').update_quality

cases = [
    Case(items[0], [9, 19]),
    Case(items[1], [1, 1]),
    Case(items[2], [4, 6]),
    Case(items[3], [0, 80]),
    Case(items[4], [14, 21]),
    Case(items[5], [2, 4]),
    Case(items[6], [3, 14]),
]


@pytest.fixture(scope='class')
def pre_test():
    update_quality()


@pytest.mark.usefixtures('pre_test')
class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_shop_inventory_manager(self, test):
        assert_true(test.test_data.sell_in, test.test_output[0])
        assert_true(test.test_data.quality, test.test_output[1])
