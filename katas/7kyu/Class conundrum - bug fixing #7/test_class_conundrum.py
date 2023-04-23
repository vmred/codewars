from asserts.asserts import assert_true
import importlib

List = importlib.import_module('katas.7kyu.Class conundrum - bug fixing #7.solution').List


class TestSolution:
    def test_class_conundrum(self):
        my_list = List(str)
        assert_true(my_list.add('Hello').count, 1)
