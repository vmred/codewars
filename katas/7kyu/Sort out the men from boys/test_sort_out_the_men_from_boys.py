import importlib
from asserts.asserts import assert_true

men_from_boys = importlib.import_module('katas.7kyu.Sort out the men from boys.solution').men_from_boys


class TestSolution:
    def test_sort_out_the_men_from_boys(self):
        assert_true(men_from_boys([72, 76, 76, 82, 100, 91, 85]), [72, 76, 82, 100, 91, 85])
