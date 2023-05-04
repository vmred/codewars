import importlib
from asserts.asserts import assert_true

maskify = importlib.import_module('katas.7kyu.Credit card mask.solution').maskify


class TestSolution:
    def test_credit_card_mask(self):
        cc = ''
        assert_true(maskify(cc), cc)

        cc = '123'
        assert_true(maskify(cc), cc)

        cc = 'SF$SDfgsd2eA'
        assert_true(maskify(cc), '########d2eA')
