from asserts.Asserts import assert_true


class TestSolution:

    def test_binary_addition(self):
        from kyu7.Binary_Addition.solution import add_binary
        assert_true(add_binary(1, 1), "10")
        assert_true(add_binary(0, 1), "1")
        assert_true(add_binary(1, 0), "1")
        assert_true(add_binary(2, 2), "100")
        assert_true(add_binary(51, 12), "111111")

    def test_regex_validate_pin_code(self):
        from kyu7.Regex_validate_PIN_code.solution import validate_pin
        assert_true(validate_pin("1"), False)
        assert_true(validate_pin("12"), False)
        assert_true(validate_pin("123"), False)
        assert_true(validate_pin("12345"), False)
        assert_true(validate_pin("1234567"), False)
        assert_true(validate_pin("-1234"), False)
        assert_true(validate_pin("1.234"), False)
        assert_true(validate_pin("-1.234"), False)
        assert_true(validate_pin("00000000"), False)

        assert_true(validate_pin("a234"), False)
        assert_true(validate_pin(".234"), False)
        assert_true(validate_pin("-123"), False)
        assert_true(validate_pin("-1.234"), False)

        assert_true(validate_pin("1234"), True)
        assert_true(validate_pin("0000"), True)
        assert_true(validate_pin("1111"), True)
        assert_true(validate_pin("123456"), True)
        assert_true(validate_pin("098765"), True)
        assert_true(validate_pin("000000"), True)
        assert_true(validate_pin("123456"), True)
        assert_true(validate_pin("090909"), True)

    def test_credit_card_mask(self):
        from kyu7.Credit_card_mask.solution import maskify
        cc = ''
        assert_true(maskify(cc), cc)

        cc = '123'
        assert_true(maskify(cc), cc)

        cc = 'SF$SDfgsd2eA'
        assert_true(maskify(cc), '########d2eA')
