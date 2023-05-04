import importlib
from asserts.asserts import assert_true

invite_more_women = importlib.import_module('katas.7kyu.Simple Fun #152 - Invite More Women.solution').invite_more_women


class TestSolution:
    def test_simple_fun_152_invite_more_women(self):
        assert_true(invite_more_women([1, -1, 1]), True)
        assert_true(invite_more_women([-1, -1, -1]), False)
        assert_true(invite_more_women([1, -1]), False)
        assert_true(invite_more_women([1, 1, 1]), True)
        assert_true(invite_more_women([]), False)
