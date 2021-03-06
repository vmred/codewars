import os

root_dir = os.path.abspath(os.pardir)


def preformat_name(name, is_test=False):
    name = ''.join(filter(lambda x: x.isalnum() or x.isspace(), name))
    if is_test:
        return '_'.join(name.lower().split())
    return name


def prepare_for_kata(kyu, directory_name, test_func_name='f'):
    kata_dir = f'{root_dir}/{kyu}/{preformat_name(directory_name)}'
    # creating directory for kata
    os.mkdir(kata_dir, 0o755)

    # creating solution.py
    open(f'{kata_dir}/solution.py', 'w+').close()

    # creating tests.py
    test_name = f'test_{preformat_name(directory_name, True)}'
    f = open(f'{kata_dir}/{test_name}.py', 'w+')
    f.write(
        f'''
import importlib

{test_func_name} = importlib.import_module('{kyu}.{directory_name}.solution').{test_func_name}


class TestSolution:
    def {test_name}(self, test_case):
        test_case.verify('', '')''')
    f.close()


prepare_for_kata('kyu6', 'Sequence of squared digits', 'squared_digits_series')
