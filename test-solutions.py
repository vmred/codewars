import os
import importlib

import unittest

suite = unittest.TestSuite()


def collect_and_run(base_subdir):
    for root, subdirs, filenames in os.walk(base_subdir):
        for subdir in subdirs:
            if not subdir.startswith('__') and subdir != 'tests':
                submodule = importlib.import_module('.'.join((root, subdir, 'solution')))

                print('\n ---> INFO:', submodule.TestSolution)

                # suite.addTest(submodule.TestSolution)
                imported = importlib.__import__(str(submodule.TestSolution))
                print('--> imported:', imported)
                suite.addTest(importlib.import_module(imported))
                print('--> suite:', suite)


if int(os.getenv('beta', '1')) == 1:
    collect_and_run('beta')


def run():
    unittest.TextTestRunner(verbosity=2).run(suite)
