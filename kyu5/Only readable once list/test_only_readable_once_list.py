from asserts.Asserts import assert_true
import importlib

SecureList = importlib.import_module('kyu5.Only readable once list.solution').SecureList


class TestSolution:

    def test_only_readable_once_list(self):
        base = [1, 2, 3, 4]
        a = SecureList(base)
        assert_true(a[0], base[0])
        assert_true(a[0], base[1])
        assert_true(len(a), 2)
        assert_true(len(a), 0)

        a = SecureList(base)
        assert_true(len(a), 0)
