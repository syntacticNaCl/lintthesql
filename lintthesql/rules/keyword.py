import sqlparse

from lintthesql.rules.rule import Rule

class KeywordRule(Rule):
    RULE_KEY = 'keyword'
    RULE_CASE_LOWER = 'lower'
    RULE_CASE_UPPER = 'upper'
    RULE_CASE_CAPITALIZE = 'capitalize'

    def get(self):
        case_rule = self.rule.get('case')

        rules = {}

        if case_rule:
            if case_rule == KeywordRule.RULE_CASE_LOWER:
                case = KeywordRule.RULE_CASE_LOWER
            elif case_rule == KeywordRule.RULE_CASE_UPPER:
                case = KeywordRule.RULE_CASE_UPPER
            elif case_rule == KeywordRule.RULE_CASE_CAPITALIZE:
                case = KeywordRule.RULE_CASE_CAPITALIZE
            else:
                raise ValueError(f'{case_rule} is not valid for the keyword case rule. Please provide a valid keyword case rule: {KeywordRule.RULE_CASE_LOWER}, {KeywordRule.RULE_CASE_UPPER}, {KeywordRule.RULE_CASE_CAPITALIZE}.')

            rules['keyword_case'] = case

        return rules

