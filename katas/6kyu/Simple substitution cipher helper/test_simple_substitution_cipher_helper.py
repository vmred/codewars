import importlib
import pytest

from asserts.asserts import assert_true
from asserts.testcase import Case

Cipher = importlib.import_module('katas.6kyu.Simple substitution cipher helper.solution').Cipher

cases_encode_cipher_one = [
    Case('a_bc&*83', 'e_ta&*83'),
    Case('abc', 'eta'),
    Case('xyz', 'qxz'),
]

cases_decode_cipher_one = [Case('eirfg', 'aeiou'), Case('erlang', 'aikcfu')]


@pytest.fixture(scope='class')
def cipher_one(request):
    request.cls.cipher = Cipher('abcdefghijklmnopqrstuvwxyz', 'etaoinshrdlucmfwypvbgkjqxz')


@pytest.mark.usefixtures('cipher_one')
class TestSolutionCipherMap1:
    @pytest.mark.parametrize(
        'test', cases_encode_cipher_one, ids=[f'{test.test_data}' for test in cases_encode_cipher_one]
    )
    def test_simple_substitution_cipher_encode_map1(self, test):
        assert_true(self.cipher.encode(test.test_data), test.test_output)  # pylint: disable=no-member

    @pytest.mark.parametrize(
        'test', cases_decode_cipher_one, ids=[f'{test.test_data}' for test in cases_decode_cipher_one]
    )
    def test_simple_substitution_cipher_decode_map1(self, test):
        assert_true(self.cipher.decode(test.test_data), test.test_output)  # pylint: disable=no-member


cases_encode_cipher_two = [
    Case('abc', 'tfo'),
    Case('ajqqtb', 'tjuukf'),
]

cases_decode_cipher_two = [Case('tfo', 'abc'), Case('kjpphi', 'tjuukf')]


@pytest.fixture(scope='class')
def cipher_two(request):
    request.cls.cipher = Cipher('abcdefghijklmnopqrstuvwxyz', 'tfozcivbsjhengarudlkpwqxmy')


@pytest.mark.usefixtures('cipher_two')
class TestSolutionCipherMap2:
    @pytest.mark.parametrize(
        'test', cases_encode_cipher_two, ids=[f'{test.test_data}' for test in cases_encode_cipher_two]
    )
    def test_simple_substitution_cipher_encode_map2(self, test):
        assert_true(self.cipher.encode(test.test_data), test.test_output)  # pylint: disable=no-member

    @pytest.mark.parametrize(
        'test', cases_decode_cipher_two, ids=[f'{test.test_data}' for test in cases_decode_cipher_two]
    )
    def test_simple_substitution_cipher_decode_map2(self, test):
        assert_true(self.cipher.decode(test.test_data), test.test_output)  # pylint: disable=no-member
