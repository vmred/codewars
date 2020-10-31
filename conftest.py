import pytest

from asserts.Asserts import TestCase


@pytest.fixture
def test_case():
    tc = TestCase()
    yield tc
    tc.is_failed()