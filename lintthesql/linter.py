from parser import Parser
from sqlparse import parse, tokens as T

class Linter(Parser):

    def lint(self):
        self.statements = parse(self.get_file_contents())
        self.all_tokens = []

        for statement in self.statements:
            for token in statement.tokens:
                if token.__class__.__name__ == 'Token':
                    self.all_tokens.append(token)
                else:
                    for token in token.tokens:
                        if token.__class__.__name__ == 'Token':
                            self.all_tokens.append(token)
                        else:
                            self.all_tokens = self.all_tokens + token.tokens

        for token in self.all_tokens:
            if self.is_valid_keyword_token(token):
                self.get_line_number(token)

    def is_valid_keyword_token(self, token):
        is_keyword_token = token.ttype in (T.Keyword.DML, T.Keyword.DDL, T.Keyword.CTE, T.Keyword.Command, T.Keyword)
        is_not_in_statement = True

        return is_keyword_token and is_not_in_statement

    def get_line_number(self, token):
        line_number = 0

        for all_token in self.all_tokens[0:self.all_tokens.index(token)]:
            if all_token.ttype in (T.Text.Whitespace.Newline, T.Comment.Single):
                line_number += 1

        print(token)
        print(line_number)
