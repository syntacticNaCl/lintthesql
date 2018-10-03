"""Test helpers"""

import io, os, pytest

from lintthesql import Config
from lintthesql.rules.keyword import KeywordRule
from lintthesql.rules.alignment import AlignmentRule
from lintthesql.rules.indent import IndentRule
from lintthesql.rules.wrap import WrapRule
from mock import Mock

@pytest.fixture()
def config_rules():
    config = Config(os.getcwd() + '/tests/files/.lintthesql.yml')
    return config.get_rules

@pytest.fixture()
def rule_indent():
    return Mock(spec=IndentRule)

@pytest.fixture()
def rule_alignment():
    return Mock(spec=AlignmentRule)

@pytest.fixture()
def rule_keyword():
    return Mock(spec=KeywordRule)

@pytest.fixture()
def rule_wrap():
    return Mock(spec=WrapRule)



