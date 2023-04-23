from asserts.asserts import assert_true
import importlib

SecureList = importlib.import_module('katas.5kyu.Only readable once list.solution').SecureList


class TestSolution:
    base = [1, 2, 3, 4]

    def test_only_readable_once_list(self):
        a = SecureList(self.base)
        assert_true(a[0], self.base[0])
        assert_true(a[0], self.base[1])
        assert_true(len(a), 2)


    def test_print_len(self):
        a = SecureList(self.base)
        print(a)
        assert_true(len(a), 0)