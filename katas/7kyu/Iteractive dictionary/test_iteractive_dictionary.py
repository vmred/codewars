import importlib
from asserts.asserts import assert_true

Dictionary = importlib.import_module('katas.7kyu.Iteractive dictionary.solution').Dictionary


class TestSolution:
    def test_iteractive_directory(self):
        d = Dictionary()

        d.newentry("Apple", "A fruit")
        assert_true(d.look("Apple"), "A fruit")

        d.newentry("Soccer", "A sport")
        assert_true(d.look("Soccer"), "A sport")
        assert_true(d.look("Hi"), "Can't find entry for Hi")
        assert_true(d.look("Ball"), "Can't find entry for Ball")
