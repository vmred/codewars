# pylint: disable=missing-module-docstring
import fileinput
import os
import sys

root_dir = os.path.abspath(os.pardir)
KATA_SOLUTION_TEMPLATE = 'katas/{}/{}/solution.py'
NEW_ENTRY_TEMPLATE = '* [{}]({}) - [codewars]({})'
SECTION_TEMPLATE = '#### <a name="{}">'


# pylint: disable=missing-function-docstring
def update_readme(kyu: str, kata_name: str, kata_url: str, kata_solution_path=None):
    kata_solution_path = kata_solution_path or KATA_SOLUTION_TEMPLATE.format(kyu, kata_name)
    kata_solution_path = kata_solution_path.replace(' ', '%20')
    new_entry = NEW_ENTRY_TEMPLATE.format(kata_name, kata_solution_path, kata_url)
    with fileinput.FileInput(os.path.join(root_dir, 'README.md'), inplace=1) as f:
        for line in f:
            if line.startswith(SECTION_TEMPLATE.format(kyu)):
                line = line.replace('\n', f'\n{new_entry}\n')

            sys.stdout.write(line)


if __name__ == '__main__':
    update_readme(kyu='kyu', kata_name='name', kata_url='url')
