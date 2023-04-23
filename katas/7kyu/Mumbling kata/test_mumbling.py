from asserts.asserts import assert_true
import importlib

accum = importlib.import_module('katas.7kyu.Mumbling kata.solution').accum


class TestSolution:
    def test_mumbling(self):
        assert_true(
            accum('ZpglnRxqenU'), 'Z-Pp-Ggg-Llll-Nnnnn-Rrrrrr-Xxxxxxx-Qqqqqqqq-Eeeeeeeee-Nnnnnnnnnn-Uuuuuuuuuuu')
