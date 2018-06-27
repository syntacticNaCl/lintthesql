# -*- coding: utf-8 -*-

import sys, os, argparse

from config import Config
from parser import Parser
from pathlib import Path

def lintthesql(args):
    input_file_path = Path(args.file)
    config_file = os.getcwd() + '/.lintthesql.yml'
    config_file_path = Path(config_file)

    if input_file_path.is_file():
        if config_file_path.is_file():
            config = Config(config_file)
            parser = Parser()
            parser.set_file(args.file)
            # print(parser.parse(config))
            print(parser.format())
        else:
            # doesn't exist
            print('Config file does not exist you dummy!')
            sys.exit()
    else:
        # doesn't exist
        print('Input file does not exist you dummy!')
        sys.exit()


def parse_args():
    arg_parser = argparse.ArgumentParser(description='Lint some SQL.')

    arg_parser.add_argument('--file', default='*', help='lints the given .sql file')

    return arg_parser.parse_args()

lintthesql(parse_args())
