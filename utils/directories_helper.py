import os


class DirectoryHelper:
    def __init__(self):
        self.root_dir = os.path.abspath(os.pardir)

    def get_root_dir(self):
        return self.root_dir

    def prepare_for_kata(self, kyu, directory_name):
        kata_dir = '{}/{}/{}'.format(self.get_root_dir(), kyu, directory_name)
        # creating directory for kata
        os.mkdir(kata_dir, 0o755)

        # creating solution.py
        open('{}/solution.py'.format(kata_dir), 'w+').close()

        # creating tests.py
        test_name = 'test_{}'.format('_'.join(directory_name.lower().split()))
        f = open('{}/{}.py'.format(kata_dir, test_name), 'w+')
        f.write('''
            from asserts.Asserts import assert_true
            import importlib
            f = importlib.import_module('{}.{}.solution').f
            
            class TestSolution:
                def {}(self):
                    pass'''.format(kyu, directory_name, test_name))
        f.close()


DirectoryHelper().prepare_for_kata('kyu8', 'Aaa Kata')
