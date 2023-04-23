from asserts.asserts import assert_true
import importlib

Cipher = importlib.import_module('katas.6kyu.Simple substitution cipher helper.solution').Cipher


class TestSolution:
    def test_simple_substitution_cipher_helper(self):
        map1 = 'abcdefghijklmnopqrstuvwxyz'
        map2 = 'etaoinshrdlucmfwypvbgkjqxz'

        cipher = Cipher(map1, map2)
        assert_true(cipher.encode('a_bc&*83'), 'e_ta&*83')
        assert_true(cipher.encode('abc'), 'eta')
        assert_true(cipher.encode('xyz'), 'qxz')
        assert_true(cipher.decode('eirfg'), 'aeiou')
        assert_true(cipher.decode('erlang'), 'aikcfu')

        map2 = 'tfozcivbsjhengarudlkpwqxmy'
        cipher = Cipher(map1, map2)
        assert_true(cipher.encode('abc'), 'tfo')
        assert_true(cipher.decode('tfo'), 'abc')
        assert_true(cipher.decode('kjpphi'), 'tjuukf')
        assert_true(cipher.encode('ajqqtb'), 'tjuukf')
