import os, sys
import yaml

from formatters.keyword import KeywordFormatter
from formatters.alignment import AlignmentFormatter

class Config:

    def __init__(self, config_path):
        self.config_path = config_path
        self.load()

    def get_rules(self):
        return self.rules

    def load(self):
        with open(self.config_path, 'r') as stream:
            try:
                self.rules = yaml.load(stream)
                return self
            except yaml.YAMLError as exc:
                print(exc)

    def get_formatters(self):
        rules = self.get_rules()
        formatters = []
        config = self.load()

        for rule in rules:
            if rule == 'keyword':
                formatter = KeywordFormatter()
                formatter.set_config(self.load())
                formatters.append(formatter)
            elif rule == 'alignment':
                formatter = AlignmentFormatter()
                formatter.set_config(self.load())
                formatters.append(formatter)

        return formatters



