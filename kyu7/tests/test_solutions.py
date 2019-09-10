from asserts.Asserts import assert_true


class TestSolution:
    def test_credit_card_mask(self):
        from kyu7.Credit_card_mask.solution import maskify
        cc = ''
        assert_true(maskify(cc), cc)

        cc = '123'
        assert_true(maskify(cc), cc)

        cc = 'SF$SDfgsd2eA'
        assert_true(maskify(cc), '########d2eA')
