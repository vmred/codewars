import importlib
from asserts.asserts import assert_true

dont_give_me_five = importlib.import_module('katas.7kyu.Dont give me five!.solution').dont_give_me_five


class TestSolution:
    def test_dont_give_me_five(self):
        assert_true(dont_give_me_five(1, 9), 8)
        assert_true(dont_give_me_five(4, 17), 12)
