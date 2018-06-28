import os, sys
import yaml

from rules.keyword import KeywordRule
from rules.alignment import AlignmentRule
from rules.indent import IndentRule

class Config:

    def __init__(self, config_path):
        self.config_path = config_path
        self.load()

    def load(self):
        with open(self.config_path, 'r') as stream:
            try:
                self.rules = yaml.load(stream)
            except yaml.YAMLError as exc:
                print(exc)

    def get_rules(self):
        rules = []

        for rule_key in self.rules:
            if rule_key == 'indent':
                rule = IndentRule()
                rule.set_rule(self.rules)
                rules.insert(0, rule)
            elif rule_key == 'keyword':
                rule = KeywordRule()
                rule.set_rule(self.rules)
                rules.append(rule)
            elif rule_key == 'alignment':
                rule = AlignmentRule()
                rule.set_rule(self.rules)
                rules.append(rule)

        return rules
