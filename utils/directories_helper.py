import os


class DirectoryHelper:
    def __init__(self):
        self.root_dir = os.path.abspath(os.pardir)

    def get_root_dir(self):
        return self.root_dir

    @staticmethod
    def preformat_name(name):
        name = ''.join([i for i in name.lower() if i.isalnum() or i.isspace()])
        return '_'.join(name.split())

    def prepare_for_kata(self, kyu, directory_name, test_func_name='f'):
        kata_dir = f'{self.get_root_dir()}/{kyu}/{directory_name}'
        # creating directory for kata
        os.mkdir(kata_dir, 0o755)

        # creating solution.py
        open(f'{kata_dir}/solution.py', 'w+').close()

        # creating tests.py
        test_name = f'test_{self.preformat_name(directory_name)}'
        f = open(f'{kata_dir}/{test_name}.py', 'w+')
        f.write(f'''
            from asserts.Asserts import assert_true
            import importlib
            {test_func_name} = importlib.import_module('{kyu}.{directory_name}.solution').{test_func_name}
            
            class TestSolution:
                def {test_name}(self):
                    assert_true('', '')''')
        f.close()


DirectoryHelper().prepare_for_kata('kyu6', 'Make the Deadfish swim', 'parse')
