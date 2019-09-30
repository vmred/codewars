from asserts.Asserts import assert_true
import importlib

Dictionary = importlib.import_module('kyu7.Iteractive dictionary.solution').Dictionary


class TestSolution:
    def test_iteractive_directory(self):
        d = Dictionary()

        d.newentry("Apple", "A fruit")
        assert_true(d.look("Apple"), "A fruit")

        d.newentry("Soccer", "A sport")
        assert_true(d.look("Soccer"), "A sport")
        assert_true(d.look("Hi"), "Can't find entry for Hi")
        assert_true(d.look("Ball"), "Can't find entry for Ball")
