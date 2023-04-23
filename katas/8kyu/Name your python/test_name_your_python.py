import importlib

from asserts.asserts import assert_true

Python = importlib.import_module('katas.8kyu.Name your python.solution').Python


class TestSolution:
    def test_name_your_python(self):
        bubba = Python('Bubba')
        assert_true(bubba.name, 'Bubba')
