import importlib
from asserts.asserts import assert_true

array_leaders = importlib.import_module('katas.7kyu.Array leaders.solution').array_leaders


class TestSolution:
    def test_array_leaders(self):
        assert_true(array_leaders([1, 2, 3, 4, 0]), [4])
        assert_true(array_leaders([16, 17, 4, 3, 5, 2]), [17, 5, 2])
