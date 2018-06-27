import os, sys, sqlparse

from formatters.formatter import Formatter

class AlignmentFormatter(Formatter):

    def get_rule(self):
        return self.rules['alignment']

    def format(self, file_contents):
        return sqlparse.format(file_contents, reindent_aligned=True)

