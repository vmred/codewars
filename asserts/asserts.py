from pytest import fail


def assert_true(actual, expected, message=''):
    if actual != expected:
        reason = f'{actual} not equal to {expected}'
        if message:
            reason = f'{reason}, reason: {message}'
        fail(reason)


class TestCase:
    def __init__(self):
        self.fail = ''

    def verify(self, actual, expected, reason=''):
        if actual != expected:
            self.fail += f'{actual} not equal to {expected}'
            self.fail += f', reason: {reason} + \n' if reason else '\n'

    def is_failed(self):
        if self.fail:
            assert False, f'{self.fail}'
