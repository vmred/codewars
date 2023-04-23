import fileinput
import os
import sys

root_dir = os.path.abspath(os.pardir)
kata_solution_path_template = 'katas/{}/{}/solution.py'
new_entry_template = '* [{}]({}) - [codewars]({})'
section_template = '#### <a name="{}">'


def update_readme(kyu: str, kata_name: str, kata_url: str, kata_solution_path=None):
    kata_solution_path = kata_solution_path or kata_solution_path_template.format(kyu, kata_name)
    new_entry = new_entry_template.format(kata_name, kata_solution_path, kata_url)
    with fileinput.FileInput(os.path.join(root_dir, 'README.md'), inplace=1) as f:
        for line in f:
            if line.startswith(section_template.format(kyu)):
                line = line.replace('\n', f'\n{new_entry}\n')

            sys.stdout.write(line)


if __name__ == '__main__':
    update_readme(kyu='8kyu', kata_name='<name>', kata_url='<url>')
