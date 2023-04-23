from asserts.asserts import assert_true
import importlib

is_valid_IP = importlib.import_module('katas.6kyu.IP validation.solution').is_valid_IP


class TestSolution:
    def test_ip_validation(self):
        assert_true(is_valid_IP('12.255.56.1'), True)
        assert_true(is_valid_IP(''), False)
        assert_true(is_valid_IP('abc.def.ghi.jkl'), False)
        assert_true(is_valid_IP('12.34.56 .1'), False)
