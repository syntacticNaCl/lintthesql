from parser import Parser
from sqlparse import parse, tokens as T
from linters.keyword import KeywordLinter

class Linter(Parser):

    def lint(self):
        self.all_tokens = self.flatten_tokens(parse(self.get_file_contents()), [])
        linting_errors = []

        for token in self.all_tokens:
            if token.is_keyword:
                keyword_linter = KeywordLinter(self.get_rule_list())

                if keyword_linter.is_invalid(token.value):
                    linting_errors.append(
                        keyword_linter.get_invalid_message(token.value, self.get_line_number(token))
                    )

        if len(linting_errors) > 0:
            self.print_file_name()

            for linting_error in linting_errors:
                print(linting_error)

    def flatten_tokens(self, tokens, flattened):
        for token in tokens:
            if token.__class__.__name__ == 'Token':
                flattened.append(token)
            else:
                self.flatten_tokens(token.tokens, flattened)

        return flattened

    def get_line_number(self, token):
        line_number = 0

        for all_token in self.all_tokens[0:self.all_tokens.index(token)]:
            if self.is_newline_token(all_token):
                line_number += 1

        return line_number

    def is_newline_token(self, token):
        return token.ttype in (T.Text.Whitespace.Newline, T.Comment.Single)

    def print_file_name(self):
        print(f'File: {self.sql_file}')
