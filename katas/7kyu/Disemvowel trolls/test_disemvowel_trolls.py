from asserts.asserts import assert_true
import importlib

disemvowel = importlib.import_module('katas.7kyu.Disemvowel trolls.solution').disemvowel


class TestSolution:
    def test_disemvowel_trolls(self):
        assert_true(disemvowel('This website is for losers LOL!'), 'Ths wbst s fr lsrs LL!')
