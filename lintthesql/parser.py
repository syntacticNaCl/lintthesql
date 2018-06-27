import os, sys

class Parser:

    def set_file(self, sql_file):
        self.file_type = self.get_file_type(sql_file)
        self.sql_file = sql_file

    def parse(self):
        if self.file_type == '.sql':
            print('Let\'s parse SQL');
        else:
            print('No valid file to use')

    def get_file_type(self, sql_file):
        return os.path.splitext(sql_file)[1]
