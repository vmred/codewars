from asserts.asserts import assert_true
import importlib

items = importlib.import_module('kyu6.Shop Inventory Manager.solution').items
update_quality = importlib.import_module('kyu6.Shop Inventory Manager.solution').update_quality


class TestSolution:
    def test_shop_inventory_manager(self):
        update_quality()
        assert_true(items[0].sell_in, 9, "Expected different value")
        assert_true(items[0].quality, 19, "Expected different value")

        assert_true(items[1].sell_in, 1, "Expected different value of sell_in")
        assert_true(items[1].quality, 1, "Expected different value of quality")

        assert_true(items[2].sell_in, 4, "Expected different value")
        assert_true(items[2].quality, 6, "Expected different value")

        assert_true(items[3].sell_in, 0, "Expected different value")
        assert_true(items[3].quality, 80, "Expected different value")

        assert_true(items[4].sell_in, 14, "Expected different value of sell_in")
        assert_true(items[4].quality, 21, "Expected different value of quality")

        assert_true(items[5].sell_in, 2, "Expected different value")
        assert_true(items[5].quality, 4, "Expected different value")

        assert_true(items[6].sell_in, 3, "Expected different value of sell_in")
        assert_true(items[6].quality, 14, "Expected different value of quality")
