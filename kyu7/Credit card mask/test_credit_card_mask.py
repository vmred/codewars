from asserts.Asserts import assert_true
import importlib

maskify = importlib.import_module('kyu7.Credit card mask.solution').maskify


class TestSolution:
    def test_credit_card_mask(self):
        cc = ''
        assert_true(maskify(cc), cc)

        cc = '123'
        assert_true(maskify(cc), cc)

        cc = 'SF$SDfgsd2eA'
        assert_true(maskify(cc), '########d2eA')
