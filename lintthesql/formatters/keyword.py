import os, sys, sqlparse

from formatters.formatter import Formatter

class KeywordFormatter(Formatter):

    def get_rule(self):
        return self.rules['keyword']

    def format(self, file_contents):
        return sqlparse.format(file_contents, reindent_aligned=True)
