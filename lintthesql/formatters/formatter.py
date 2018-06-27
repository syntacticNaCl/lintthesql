import sys

from sqlparse import tokens as T
from sqlparse import sql, parse, format as sqlformat

class Formatter(object):

    def set_config(self, config):
        try:
            self.rules = config.get_rules()
        except:
            print('Please provide a valid Config object to the parser')
            sys.exit()

    def get_rule(self):
        pass

    def format(self):
        pass

    def fix_spacing(self, sql_formatted):
        sql_formatted = sql_formatted.replace('--', '\n--')
        return sql_formatted
    
