from asserts.Asserts import assert_true
import importlib

song_decoder = importlib.import_module('kyu6.Dubstep kata.solution').song_decoder


class TestSolution:
    def test_dubstep_kata(self):
        assert_true(song_decoder("AWUBBWUBC"), "A B C")
        assert_true(song_decoder("AWUBWUBWUBBWUBWUBWUBC"), "A B C")
