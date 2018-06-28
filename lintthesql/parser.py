import os, sys, sqlparse

from config import Config
from formatter import Formatter

class Parser:

    def __init__(self, config):
        if isinstance(config, Config):
            self.config = config
            self.rules = config.get_rules()
        else:
            raise Exception('Please provide a valid Config object to the parser')

    def set_file(self, sql_file):
        """
        Set the file and various metadata.
        """
        self.file_type = self.get_file_extension(sql_file)
        self.sql_file = sql_file

    def parse(self, config):
        if self.file_type == '.sql':
            return self.rulesget_tokens(self.get_file_contents())
        else:
            print('No valid file to use')

    def get_file_extension(self, sql_file):
        """
        Get the file extension for the provided file.
        """
        return os.path.splitext(sql_file)[1]


    def get_file_contents(self):
        """
        Read the raw contents of the file.
        """
        with open(self.sql_file, 'r') as sql:
            text = sql.read()
            # text = text.replace('\n', '\n\n')
            # text=sql.read()
            # TODO: fix some text replacement issues here
            # https://github.com/andialbrecht/sqlparse/issues/313
        return self.filter_text(text)

    def get_tokens(self, sql_text):
        """
        Return all tokens retrieved from raw sql text.
        """
        parsed = sqlparse.parse(sql_text)[0]
        return parsed.tokens

    def format(self):
        file_contents = self.get_file_contents()
        formatter = Formatter()
        file_contents = formatter.format(file_contents, **self.get_rule_list())

        print(file_contents)

    def get_rule_list(self):
        rules = self.config.get_rules()
        rule_list = {}

        for rule in rules:
            rule_list = {**rule_list, **rule.get()}

        return rule_list

    def filter_text(self, text):
        return text.replace(";\n",";").replace("--","\n--")
