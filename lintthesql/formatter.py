import os, sys, sqlparse

from config import Config

class Formatter():

    KEYWORD_LENGTH = 0

    STRING_DELIMITERS = ['"']

    def __init__(self, custom = False):
        self.custom = custom
        # self.token_metadata = {}
        self.snapshots = {'strings': {}}

    def format(self, file_contents, **rule_list):
        if self.custom:
            return self.format_custom(file_contents, **rule_list)

        snapshot = self.create_snapshot(file_contents)

        formatted = sqlparse.format(file_contents, **rule_list)

        post_process = self.post_process(formatted)

        return post_process

    def format_custom(self, file_contents, **rule_list):
        statements = sqlparse.parse(file_contents)
        statement_raw = ''

        for statement in statements:
            skip = False
            keyword_length = 0
            token_list = sqlparse.sql.TokenList(statement.tokens)

            for token in statement.tokens:
                token_idx = token_list.token_index(token)
                self.set_token_metadata(token_idx, token)

                if token.value == '"' and skip:
                    skip = False
                    statement_raw += token.value
                    continue

                if token.value == '"':
                    skip = True
                    statement_raw += token.value
                    continue
                elif skip == True:
                    statement_raw += token.value
                    continue

                statement_raw += self.token_handler(token)

            return statement_raw

    def token_handler(self, token):
        pass
        if token.ttype is None:
            return token.value

        if 'DML' in token.ttype:
            print('Statement start')
            return token.value.replace('\n', '')
        elif 'Keyword' in token.ttype:
            print('Keyword')

        return token.value

    def set_token_metadata(self, token_idx, token):
        """
        Parameters
        -----------
        token_idx : int
        token : sqlparse.sql.Token

        Returns
        __________
        void
        """
        pass
        if self.KEYWORD_LENGTH < len(token.value):
            self.KEYWORD_LENGTH - len(token.value)

        self.token_metadata[token_idx] = {'name': token.value, 'type': token.ttype, 'space_before': 0, 'space_after': 0}

    def create_snapshot(self, file_contents):

        for statement in sqlparse.parse(file_contents):
            strings = self.get_strings(statement)
            if strings:
                self.snapshots['strings'] = strings

    def post_process(self, formatted_text):
        statements = sqlparse.parse(formatted_text)
        for idx, statement in enumerate(statements):
            new_strings = self.get_strings(statement)
            if new_strings:
                return formatted_text.replace(new_strings[idx], self.snapshots['strings'][idx])

    def get_strings(self, statement):
        skip = False
        token_list = sqlparse.sql.TokenList(statement.tokens)
        statement_raw = ''
        string_list = []

        for token in statement.tokens:
            if token.value == '"' and skip:
                skip = False
                statement_raw += token.value
                string_list.append(statement_raw)
                continue

            if token.value == '"':
                skip = True
                statement_raw += token.value
                continue
            elif skip == True:
                statement_raw += token.value
                continue

        return string_list
