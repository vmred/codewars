# pylint: disable=missing-module-docstring
import os

root_dir = os.path.abspath(os.pardir)


def preformat_name(name, is_test=False):  # pylint: disable=missing-function-docstring
    name = ''.join(filter(lambda x: x.isalnum() or x.isspace(), name))
    if is_test:
        return '_'.join(name.lower().split())
    return name


def prepare_for_kata(kyu, directory_name, test_func_name='f'):  # pylint: disable=missing-function-docstring
    kata_dir = f'{root_dir}/katas/{kyu}/{preformat_name(directory_name)}'
    # creating directory for kata
    os.mkdir(kata_dir, 0o755)

    # creating solution.py
    with open(f'{kata_dir}/solution.py', 'w+', encoding='utf-8') as _:
        pass

    # creating tests.py
    test_name = f'test_{preformat_name(directory_name, True)}'
    with open(f'{kata_dir}/{test_name}.py', 'w+', encoding='utf-8') as f:
        f.write(
            f'''
import importlib
import pytest
from asserts.asserts import assert_true
from asserts.testcase import TestCase
    
solution = importlib.import_module('katas.{kyu}.{directory_name}.solution').{test_func_name}
    
cases = [
    TestCase()
]
    
class TestSolution:
    
    @pytest.mark.parametrize('test', cases, ids=[f'{{test.test_data}}' for test in cases])
    def {test_name}(self, test):
        assert_true(solution(test.test_data), test.test_output)
'''
        )


if __name__ == '__main__':
    prepare_for_kata('kyu', 'name', 'solution')
