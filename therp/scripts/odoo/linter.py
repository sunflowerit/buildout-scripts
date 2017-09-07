# -*- coding: utf-8 -*-
from argparse import ArgumentParser
import os 
from pylint.lint import Run


def do_pylint():
    parser = ArgumentParser()
    parser.add_argument('repo_to_lint', metavar='repo', type=str,
                        help='the name of the repo to run PyLint on')
    arguments = parser.parse_args()
    cur_path = os.getcwd()
    repo_to_lint = os.path.join(cur_path, 'parts', arguments.repo_to_lint)
    for path_to_lint in os.listdir(repo_to_lint):
        if not os.path.isfile(path_to_lint):
            Run(['--rcfile=.pylint.cfg', path_to_lint])

