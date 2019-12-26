import requests

hostname = 'https://google.com'


def log_call(func):
    def wrapper(*args, **kwargs):
        print(kwargs)
        print(args)
        args, args[1] = list(args), f'{hostname}{args[1]}'
        args = tuple(args)
        print(args)
        result = func(*args, **kwargs)
        print(result.url)
        return result

    return wrapper


class A:
    def __init__(self):
        pass

    @log_call
    def get1(self, *args, **kwargs):
        return requests.get(*args, **kwargs)


a = A()
r = a.get1('', headers={})
print(r.status_code)
print(r.content)
