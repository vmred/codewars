from asserts.asserts import assert_true
import importlib

song_decoder = importlib.import_module('katas.6kyu.Dubstep.solution').song_decoder


class TestSolution:
    def test_dubstep_kata(self):
        assert_true(song_decoder("AWUBBWUBC"), "A B C")
        assert_true(song_decoder("AWUBWUBWUBBWUBWUBWUBC"), "A B C")
