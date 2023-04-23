from asserts.asserts import assert_true
import importlib

find_short = importlib.import_module('katas.7kyu.Shortest word.solution').find_short


class TestSolution:
    def test_shortest_word(self):
        assert_true(find_short("bitcoin take over the world maybe who knows perhaps"), 3)
        assert_true(find_short("Lets all go on holiday somewhere very cold"), 2)
