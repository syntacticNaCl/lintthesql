import os, sys, sqlparse

from config import Config

class Parser:

    def set_file(self, sql_file):
        """
        Set the file and various metadata.
        """
        self.file_type = self.get_file_extension(sql_file)
        self.sql_file = sql_file

    def parse(self, config):
        if self.file_type == '.sql':
            if isinstance(config, Config):
                rules = config.get_rules()

                return self.get_tokens(self.get_file_contents())
                return rules
            else:
                raise Exception('Please provide a valid Config object to the parser')
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
            text = text.replace(";\n",";")
            text = text.replace("--","\n--")
            # text = text.replace('\n', '\n\n')
            # text=sql.read()
            # TODO: fix some text replacement issues here
            # https://github.com/andialbrecht/sqlparse/issues/313
        return text

    def get_tokens(self, sql_text):
        """
        Return all tokens retrieved from raw sql text.
        """
        parsed = sqlparse.parse(sql_text)[0]
        return parsed.tokens

    def format(self):
        return sqlparse.format(self.get_file_contents(), reindent_aligned=True)
