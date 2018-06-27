# -*- coding: utf-8 -*-

import sys, os, argparse

from config import Config
from parser import Parser
from pathlib import Path

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

    parser = Parser()
    input_file = cwd + '/' + args.file
    input_file_path = Path(input_file)

    if input_file_path.is_file():
        parse(parser, input_file)
    elif input_file_path.is_dir():
        for root, dirs, files in os.walk(input_file_path):
            path = root.split(os.sep)

            for file in files:
                input_file = root + '/' + file

                if os.path.splitext(input_file)[1] == '.' + args.type.replace('.', ''):
                    parse(parser, input_file)
    else:
        # doesn't exist
        print('Input file does not exist you dummy!')
        sys.exit()

def parse_args():
    arg_parser = argparse.ArgumentParser(description='Lint some SQL.')

    arg_parser.add_argument('--file', default='./', help='lints the given .sql file')
    arg_parser.add_argument('--type', default='sql', help='sets the type of files to lint (default: .sql)')

    return arg_parser.parse_args()

def parse(parser, file):
    parser.set_file(file)
    # print(parser.parse(config))
    print(parser.format())

lintthesql(parse_args())
