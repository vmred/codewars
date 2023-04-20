from asserts.asserts import assert_true
import importlib

encrypt = importlib.import_module('katas.kyu6.Simple encryption 1.solution').encrypt
decrypt = importlib.import_module('katas.kyu6.Simple encryption 1.solution').decrypt


class TestSolution:
    def test_simple_encryption_1(self):
        assert_true(encrypt('This is a test!', 1), 'hsi  etTi sats!')
        assert_true(decrypt('hsi  etTi sats!', 1), 'This is a test!')
        assert_true(encrypt('This is a test!', 3), ' Tah itse sits!')
