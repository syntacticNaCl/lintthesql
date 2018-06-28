import sys

from sqlparse import tokens as T
from sqlparse import sql, parse, format as sqlformat

class Rule(object):
    RULE_KEY = None

    def set_rule(self, rules):
        self.rule = rules.get(self.RULE_KEY)

    def format(self):
        pass

    def fix_spacing(self, sql_formatted):
        sql_formatted = sql_formatted.replace('--', '\n--')
        return sql_formatted
