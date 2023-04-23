from asserts.asserts import assert_true
import importlib

score = importlib.import_module('katas.5kyu.Greed is good.solution').score


class TestSolution:

    def test_greed_is_good(self):
        assert_true(score([2, 3, 4, 6, 2]), 0)
        assert_true(score([4, 4, 4, 3, 3]), 400)
        assert_true(score([2, 4, 4, 5, 4]), 450)
        assert_true(score([1, 1, 1, 1]), 1100)
        assert_true(score([1, 1, 1, 3, 3]), 1000)
