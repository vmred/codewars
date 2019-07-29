from pytest import fail


def assert_true(actual, expected):
    if actual != expected:
        fail('--> {} not equal to {}'.format(actual, expected))
