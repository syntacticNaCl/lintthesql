import sqlparse

from rules.rule import Rule

class KeywordRule(Rule):
    RULE_CASE_LOWER = 'lower'
    RULE_CASE_UPPER = 'upper'
    RULE_CASE_CAPITALIZE = 'capitalize'

    def __init__(self):
        self.rule_key = 'keyword'

    def format(self, file_contents):
        rule = self.rule
        case_rule = rule['case']

        if case_rule:
            if case_rule == KeywordRule.RULE_CASE_LOWER:
                file_contents = self.format_with_sqlparse(file_contents, KeywordRule.RULE_CASE_LOWER)
            elif case_rule == KeywordRule.RULE_CASE_UPPER:
                file_contents = self.format_with_sqlparse(file_contents, KeywordRule.RULE_CASE_UPPER)
            elif case_rule == KeywordRule.RULE_CASE_CAPITALIZE:
                file_contents = self.format_with_sqlparse(file_contents, KeywordRule.RULE_CASE_CAPITALIZE)
            else:
                raise ValueError(f'{case_rule} is not valid for the keyword case rule. Please provide a valid keyword case rule: {KeywordRule.RULE_CASE_LOWER}, {KeywordRule.RULE_CASE_UPPER}, {KeywordRule.RULE_CASE_CAPITALIZE}.')

        return file_contents

    def format_with_sqlparse(self, file_contents, case):
        return sqlparse.format(file_contents, keyword_case=case)
