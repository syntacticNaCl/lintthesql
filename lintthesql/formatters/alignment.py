import os, sys

from sqlparse import tokens as T
from sqlparse import sql, parse, format as sqlformat

from formatters.formatter import Formatter

class AlignmentFormatter(Formatter):

    def get_rule(self):
        return self.rules['alignment']

    def format(self, file_contents):
        rule = self.get_rule()

        # TODO: parse tokens before passing to formatter. need to fix spacing after terminators and line endings

        if rule['justification'] and rule['justification'] != 'left':
            formattedSql = sqlformat(file_contents, reindent_aligned=True)
        else:
            formattedSql = sqlformat(file_contents, reindent=True)

        return self.fix_spacing(formattedSql)

