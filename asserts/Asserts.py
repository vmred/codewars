from pytest import fail


def assert_true(actual, expected, message=''):
    if actual != expected:
        reason = f'{actual} not equal to {expected}'
        if message:
            reason = f'{reason}, reason: {message}'
        fail(reason)
