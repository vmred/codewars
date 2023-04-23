import importlib

from asserts.asserts import assert_true

contain_all_rots = importlib.import_module('katas.7kyu.All inclusive.solution').contain_all_rots


class TestSolution:
    def test_all_inclusive(self):
        # assert_true(contain_all_rots('', []), True)
        assert_true(contain_all_rots("bsjq", ["bsjq", "qbsj", "sjqb", "twZNsslC", "jqbs"]), True)
        # assert_true(contain_all_rots('ZmzTmUpEmsI',
        #                              ['IZmzTmUpEms', 'sIZmzTmUpEm', 'zTmUpEmsIZm', 'mUpEmsIZmzT', 'EmsIZmzTmUp',
        #                               'pEmsIZmzTmU', 'ZmzTmUpEmsI', 'mzTmUpEmsIZ', 'UpEmsIZmzTm', 'msIZmzTmUpE',
        #                               'TmUpEmsIZmz']), False)
