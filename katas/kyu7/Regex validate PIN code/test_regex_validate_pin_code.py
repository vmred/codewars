from asserts.asserts import assert_true
import importlib

validate_pin = importlib.import_module('katas.kyu7.Regex validate PIN code.solution').validate_pin


class TestSolution:
    def test_regex_validate_pin_code(self):
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
