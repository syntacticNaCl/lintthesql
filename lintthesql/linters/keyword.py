from linters.abstract import AbstractLinter
from rules.keyword import KeywordRule

class KeywordLinter(AbstractLinter):
    def configure_rule(self, rules):
        self.case_rule = rules['keyword_case']

    def is_invalid(self, value):
        case_rule = self.case_rule

        if case_rule == KeywordRule.RULE_CASE_LOWER:
            return value.islower() == False
        elif case_rule == KeywordRule.RULE_CASE_UPPER:
            return value.isupper() == False
        elif case_rule == KeywordRule.RULE_CASE_CAPITALIZE:
            return value[0].isupper() == False or value[1:-1].islower() == False

    def get_invalid_message(self, value, line_number):
        return f'Line {line_number}: "{value}" should be {self.get_expected_case()}.'

    def get_expected_case(self):
        case_rule = self.case_rule

        if case_rule == KeywordRule.RULE_CASE_LOWER:
            return 'lowercase'
        elif case_rule == KeywordRule.RULE_CASE_UPPER:
            return 'uppercase'
        elif case_rule == KeywordRule.RULE_CASE_CAPITALIZE:
            return 'capitalized'
