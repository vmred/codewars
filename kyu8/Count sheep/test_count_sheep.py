from asserts.asserts import assert_true
import importlib

count_sheeps = importlib.import_module('kyu8.Count sheep.solution').count_sheeps


class TestSolutions:
    def test_count_sheep(self):
        array1 = [True, True, True, False,
                  True, True, True, True,
                  True, False, True, False,
                  True, False, False, True,
                  True, True, True, True,
                  False, False, True, True]

        assert_true(count_sheeps(array1), 17)
