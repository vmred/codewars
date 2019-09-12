from asserts.Asserts import assert_true
import importlib

Vector = importlib.import_module('kyu5.Vector class.solution').Vector


class TestSolution:

    def test_vector_class(self):
        a = Vector([1, 2])
        b = Vector([3, 4])

        assert_true(Vector([1, 2, 3]).__str__(), '(1,2,3)')
        assert_true(a.add(b).equals(Vector([4, 6])), True)
        a = Vector([1, 2, 3])
        assert_true(a.norm(), 14 ** 0.5)
