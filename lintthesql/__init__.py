# -*- coding: utf-8 -*-

import sys, os, argparse

from config import Config
from parser import Parser
from pathlib import Path

def lintthesql(input):
    input_file_path = Path(input)
    config_file = os.getcwd() + '/.lintthesql.yml'
    config_file_path = Path(config_file)

    if input_file_path.is_file():
        print('Exists')
        parser = Parser()
        parser.set_file(input)
        print(parser.parse())
    else:
        # doesn't exist
        print('File does not exist you dummy!')
        sys.exit()

    if config_file_path.is_file():
        config = Config(config_file)
        print(config.get_rules())
    else:
        # doesn't exist
        print('File does not exist you dummy!')
        sys.exit()

lintthesql(sys.argv[1])

