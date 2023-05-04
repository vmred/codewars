import importlib
from asserts.asserts import assert_true

generateShape = importlib.import_module('katas.7kyu.Build the square.solution').generateShape


class TestSolution:
    def test_build_the_square(self):
        assert_true(generateShape(3), '+++\n+++\n+++')
        assert_true(generateShape(8), '++++++++\n++++++++\n++++++++\n++++++++\n++++++++\n++++++++\n++++++++\n++++++++')
