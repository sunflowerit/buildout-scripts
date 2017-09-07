# -*- coding: utf-8 -*-
from argparse import ArgumentParser
import os 
from pylint.lint import Run


def do_pylint():
    parser = ArgumentParser()
    parser.add_argument('path_to_lint', metavar='folder', type=str,
                        help='the folder of the module(s) to run PyLint on')
    arguments = parser.parse_args()
    cur_path = os.getcwd()
    path_to_lint = os.path.join(cur_path, arguments.path_to_lint)
    Run(['--rcfile=.pylint.cfg', path_to_lint])

