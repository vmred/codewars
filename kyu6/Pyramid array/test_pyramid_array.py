from asserts.asserts import assert_true
import importlib

pyramid = importlib.import_module('kyu6.Pyramid array.solution').pyramid


class TestSolution:
    def test_pyramid_array(self):
        assert_true(pyramid(0), [])
        assert_true(pyramid(1), [[1]])
        assert_true(pyramid(2), [[1], [1, 1]])
        assert_true(pyramid(3), [[1], [1, 1], [1, 1, 1]])
