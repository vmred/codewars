import importlib
from asserts.asserts import assert_true

nb_year = importlib.import_module('katas.7kyu.Growth of population.solution').nb_year


class TestSolution:
    def test_growth_of_population(self):
        assert_true(nb_year(1500, 5, 100, 5000), 15)
        assert_true(nb_year(1500000, 2.5, 10000, 2000000), 10)
        assert_true(nb_year(1500000, 0.25, 1000, 2000000), 94)
