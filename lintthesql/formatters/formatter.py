import sys

from sqlparse import tokens as T
from sqlparse import sql, parse, format as sqlformat

class Formatter(object):

    PRIORITY=None

    def set_config(self, config):
        rules = config.get_rules()
        self.rule = rules.get(self.rule_key)

    def get_rule(self):
        pass

    def format(self):
        pass

    def fix_spacing(self, sql_formatted):
        sql_formatted = sql_formatted.replace('--', '\n--')
        return sql_formatted
