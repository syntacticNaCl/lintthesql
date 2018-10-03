import os
import pytest
from lintthesql.rules.keyword import KeywordRule
from lintthesql import Config
from mock import patch

def test_rule_config(config_rules):
    config = Config(os.getcwd() + '/tests/files/.lintthesql.yml')
    rules = config.get_rules()

    for rule in rules:
        if isinstance(rule, KeywordRule):
            rule = rule
            break

    rules = rule.get()

    assert rules == {"keyword_case": 'upper'}
