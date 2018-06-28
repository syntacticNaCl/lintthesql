import os, sys

from sqlparse import tokens as T
from sqlparse import sql, parse, split, format as sqlformat

from lintthesql.rules.rule import Rule

class WrapRule(Rule):
    RULE_KEY = 'wrap'

    def get(self):
        if self.rule['column_limit'] > 0:
            return { 'wrap_after': self.rule['column_limit'] }

