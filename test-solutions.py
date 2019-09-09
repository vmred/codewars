import os
import importlib


def collect_and_run(base_subdir):
    for root, subdirs, filenames in os.walk(base_subdir):
        for subdir in subdirs:
            if not subdir.startswith('__'):
                print('-->Info: root directory:', root, ', subdir:', subdir)
                submodule = importlib.import_module('.'.join((root, subdir, 'solution')))
                submodule.test()


if int(os.getenv('beta', '1')) == 1:
    collect_and_run('beta')
