import os
import pytest
from mock import patch
# from pytest_mock import mocker
from lintthesql import Config
from lintthesql.rules.keyword import KeywordRule
from lintthesql.rules.alignment import AlignmentRule
from lintthesql.rules.indent import IndentRule
from lintthesql.rules.wrap import WrapRule

def test_config_setup(rule_indent, config_rules):
    rules = config_rules()
    assert isinstance(rules[0], IndentRule)
    assert isinstance(rules[1], AlignmentRule)
    assert isinstance(rules[2], KeywordRule)
    assert isinstance(rules[3], WrapRule)
    assert len(rules) is not 0

