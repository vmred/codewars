from asserts.asserts import assert_true
import importlib

order = importlib.import_module('katas.6kyu.Your orders please.solution').order


class TestSolution:
    def test_your_orders_please(self):
        assert_true(order('is2 Thi1s T4est 3a'), 'Thi1s is2 3a T4est')
        assert_true(order('4of Fo1r pe6ople g3ood th5e the2'), 'Fo1r the2 g3ood 4of th5e pe6ople')
