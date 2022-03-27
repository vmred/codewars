from asserts.asserts import assert_true
import importlib

Vector = importlib.import_module('kyu5.Vector class #1.solution').Vector


class TestSolution:
    def test_vector_class_1(self):
        examples = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]

        assert_true(Vector(examples[0]), Vector(*examples[0]))
        v = Vector(examples[1])
        assert_true(v.x, 4)
        assert_true(v.y, 5)
        assert_true(v.z, 6)
        assert_true(Vector(examples[0]).magnitude, 3.7416573867739413)
        assert_true(Vector(examples[2]).to_tuple(), tuple(examples[2]))
        assert_true(str(Vector(examples[1])), "<4, 5, 6>")

        assert_true(Vector(examples[0]) + Vector(*examples[1]), Vector(5, 7, 9))
        assert_true(Vector(examples[0]) - Vector(*examples[2]), Vector(-6, -6, -6))
        assert_true(Vector(examples[0]).cross(Vector(*examples[1])), Vector(-3, 6, -3))
        assert_true(Vector(examples[1]).dot(Vector(*examples[2])), 122)
