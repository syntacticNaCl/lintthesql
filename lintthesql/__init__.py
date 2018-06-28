# -*- coding: utf-8 -*-

import sys, os, argparse, time, atexit

from config import Config
from linter import Linter
from pathlib import Path
from nyanbar import NyanBar

def lintthesql(args):
    cwd = os.getcwd()
    config_file = cwd + '/.lintthesql.yml'
    config_file_path = Path(config_file)

    if config_file_path.is_file():
        config = Config(config_file)
    else:
        # doesn't exist
        print('Config file does not exist you dummy!')
        sys.exit()

    linter = Linter(config)
    should_rewrite = args.fix
    input_file = cwd + '/' + args.file
    input_file_path = Path(input_file)

    if input_file_path.is_file():
        try:
            lint_file(linter, input_file)
        except ValueError as error:
            print(error)
    elif input_file_path.is_dir():
        input_files = []

        for root, dirs, files in os.walk(input_file_path):
            path = root.split(os.sep)

            for file in files:
                input_file = root + '/' + file

                if os.path.splitext(input_file)[1] == '.' + args.type.replace('.', ''):
                    input_files.append(input_file)

        total_input_files = len(input_files)

        for input_file in input_files:
            try:
                lint_file(linter, input_file)
            except ValueError as error:
                print(error)

            input_file_index = input_files.index(input_file)
            progress = (input_file_index + 1) / total_input_files * 100

            if nyan_progress:
                nyan_progress.update(progress)
    else:
        # doesn't exist
        print('Input file does not exist you dummy!')
        sys.exit()

def parse_args():
    arg_parser = argparse.ArgumentParser(description='Lint, the S(e)Q(ue)L - a configurable SQL linter.')

    arg_parser.add_argument('--file', default='./', help='lints the given file (default: lints all files)')
    arg_parser.add_argument('--type', default='sql', help='sets the type of files to lint (default: .sql)')
    arg_parser.add_argument('--fix', default=False, action='store_true', help='will re-write the SQL statements in files when ran (default: false)')
    arg_parser.add_argument('--nyan', default=False, action='store_true', help='show a Nyan Cat progress bar')

    return arg_parser.parse_args()

def lint_file(linter, file):
    linter.set_file(file)

    if args.fix:
        linter.format()
    else:
        linter.lint()

@atexit.register
def clean_up():
    if nyan_progress:
        nyan_progress.finish()

args = parse_args()
nyan_progress = None

if args.nyan:
    nyan_mp3_file = os.path.dirname(__file__) + '/nyan.mp3'
    nyan_progress = NyanBar(audiofile=nyan_mp3_file)

lintthesql(args)
