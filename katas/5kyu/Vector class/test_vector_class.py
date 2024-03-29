import importlib
from asserts.asserts import assert_true

Vector = importlib.import_module('katas.5kyu.Vector class.solution').Vector


class TestSolution:
    def test_vector_class(self):
        a = Vector([1, 2])
        b = Vector([3, 4])

        assert_true(Vector([1, 2, 3]).__str__(), '(1,2,3)')  # pylint: disable=unnecessary-dunder-call
        assert_true(a.add(b).equals(Vector([4, 6])), True)
        a = Vector([1, 2, 3])
        assert_true(a.norm(), 14**0.5)
