import os, sys

from sqlparse import tokens as T
from sqlparse import sql, parse, split, format as sqlformat

from rules.rule import Rule

class AlignmentRule(Rule):
    RULE_KEY = 'alignment'

    def get(self):
        if self.rule['justification'] and self.rule['justification'] != 'left':
            return { 'reindent_aligned': True }

        return { 'reindent': True }

    def format(self, file_contents):
        rule = self.rule

        # TODO: parse tokens before passing to rule. need to fix spacing after terminators and line endings

        if rule['justification'] and rule['justification'] != 'left':
            formattedSql = sqlformat(file_contents, reindent_aligned=True)
        else:
            formattedSql = sqlformat(file_contents, reindent=True)

        return self.fix_spacing(formattedSql)

    def format_custom(self, file_contents):
        statements = parse(file_contents)
        statement = statements[0]
        for token in statement:
            print(token.ttype)
        return statement

