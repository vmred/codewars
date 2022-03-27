from asserts.asserts import assert_true
import importlib

mix_fruit = importlib.import_module('kyu6.Mix Fruit Juice.solution').mix_fruit


class TestSolution:
    def test_mix_fruit_juice(self):
        assert_true(mix_fruit(["banana", "mango", "avocado"]), 6)
        assert_true(mix_fruit(["melon", "Mango", "kiwi"]), 8)
        assert_true(mix_fruit(["watermelon", "cherry", "avocado"]), 8)
        assert_true(mix_fruit(["watermelon", "lime", "tomato"]), 9)
        assert_true(mix_fruit(["blackBerry", "coconut", "avocado"]), 8)
        assert_true(mix_fruit(["waterMelon", "mango"]), 8)
        assert_true(mix_fruit(["watermelon", "pEach"]), 9)
        assert_true(mix_fruit(["watermelon", "Orange", "grapes"]), 6)
        assert_true(mix_fruit(["watermelon"]), 9)
        assert_true(mix_fruit(["BlACKbeRrY", "cOcONuT", "avoCaDo"]), 8)