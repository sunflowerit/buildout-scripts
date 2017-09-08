# -*- coding: utf-8 -*-
from argparse import ArgumentParser
import os 
from pylint.lint import Run


def do_pylint():
    parser = ArgumentParser()
    parser.add_argument('repo_to_lint', metavar='repo', type=str,
                        help='the name of the repo to run PyLint on')
    arguments = parser.parse_args()
    script_path = os.path.dirname(os.path.abspath(__file__))
    base_dir = os.path.join(script_path, '../../../..')
    repo_to_lint = os.path.join(base_dir, 'parts', arguments.repo_to_lint)
    rc_file = os.path.join(base_dir, '.pylint.cfg')
    for path_to_lint in sorted(os.listdir(repo_to_lint)):
        full_path_to_lint = os.path.join(repo_to_lint, path_to_lint)
        if os.path.isfile(os.path.join(full_path_to_lint, '__init__.py')):
            Run(['--rcfile=' + rc_file, 
            '--load-plugins=pylint_odoo', 
            full_path_to_lint], exit=False)
