# -*- coding: utf-8 -*-

import sys, os

from config import Config
from pathlib import Path

def lintthesql(input):
    input_file = Path(input)
    config_file = os.getcwd() + '/.lintthesql.yml'
    config_file_path = Path(config_file)

    if input_file.is_file():
        print('Exists')
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

lintthesql(sys.argv[0])

