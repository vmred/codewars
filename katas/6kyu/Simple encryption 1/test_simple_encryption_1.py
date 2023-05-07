import importlib
import pytest

from asserts.asserts import assert_true
from asserts.testcase import Case

encrypt = importlib.import_module('katas.6kyu.Simple encryption 1.solution').encrypt
decrypt = importlib.import_module('katas.6kyu.Simple encryption 1.solution').decrypt

cases_encrypt = [Case(['This is a test!', 1], 'hsi  etTi sats!'), Case(['This is a test!', 3], ' Tah itse sits!')]

cases_decrypt = [
    Case(['hsi  etTi sats!', 1], 'This is a test!'),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases_encrypt, ids=[f'{test.test_data}' for test in cases_encrypt])
    def test_simple_encryption_1_encrypt(self, test):
        assert_true(encrypt(*test.test_data), test.test_output)

    @pytest.mark.parametrize('test', cases_decrypt, ids=[f'{test.test_data}' for test in cases_decrypt])
    def test_simple_encryption_1_decrypt(self, test):
        assert_true(decrypt(*test.test_data), test.test_output)
