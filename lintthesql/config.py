import os, sys
import yaml

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
            except yaml.YAMLError as exc:
                print(exc)


