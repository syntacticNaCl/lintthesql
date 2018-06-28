import os, sys

from sqlparse import tokens as T
from sqlparse import sql, parse, split, format as sqlformat

from formatters.formatter import Formatter

class IndentFormatter(Formatter):

    PRIORITY = 'high'

    def __init__(self):
        self.rule_key = 'indent'

    def format(self, file_contents):
        rule = self.rule

        # TODO: parse tokens before passing to formatter. need to fix spacing after terminators and line endings
        has_tabs = rule.get('tabs', False)
        width = rule.get('width', False)

        return sqlformat(file_contents, indent_width=width)

