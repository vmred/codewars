import requests

hostname = 'https://google.com'


class RequestDecorator:
    def __init__(self, function):
        self.function = function

    def __call__(self, *args, **kwargs):
        print(self.function.__name__.upper())
        response = self.function(*args, **kwargs)(f'{hostname}{args[0]}', *args, **kwargs)
        print(response.url)
        print(response)
        return response


class A:
    def __init__(self):
        pass

    @RequestDecorator
    def get1(self):
        return requests.get


a = A()
r = a.get1(
    '/search?sxsrf=ACYBGNT_JcVuYPHESDHw_aCpyWYosO4_Wg%3A1577359977825&source=hp&ei=aZoEXsmLMOOyrgTdi4j4Bg&q=e&oq=e&gs_l=psy-ab.3..35i39j0j0i131j0l2j0i131l2j0j0i10i1j0i131.4650.6033..6438...6.0..0.89.174.2......0....1..gws-wiz.....10..35i362i39j0i67j0i20i263.AjqszVBS4qw&ved=0ahUKEwiJ5KLpm9PmAhVjmYsKHd0FAm8Q4dUDCAY&uact=5')
print(r.status_code)
print(r.content)
