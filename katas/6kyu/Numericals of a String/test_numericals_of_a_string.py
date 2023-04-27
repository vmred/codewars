from asserts.asserts import assert_true
import importlib

numericals = importlib.import_module('katas.6kyu.Numericals of a String.solution').numericals


class TestSolution:
    def test_numericals_of_a_string(self):
        assert_true(numericals("Hello, World!"), "1112111121311")
        assert_true(numericals("Hello, World! It's me, JomoPipi!"), "11121111213112111131224132411122")
