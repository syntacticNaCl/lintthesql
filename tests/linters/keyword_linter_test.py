from lintthesql.linters.keyword import KeywordLinter

import os
import pytest
from mock import patch

def test_is_invalid():
    linter = KeywordLinter({'keyword_case': 'upper'})
    linter.configure_rule({'keyword_case': 'upper'})

    assert linter.is_invalid('foo')
    assert not linter.is_invalid('FOO')

def test_get_invalid_message_upper():
    linter = KeywordLinter({'keyword_case': 'upper'})
    invalid_message = linter.get_invalid_message('test', 1)
    assert invalid_message == 'Line 1: "test" should be uppercase.'

def test_get_invalid_message_lower():
    linter = KeywordLinter({'keyword_case': 'lower'})
    invalid_message = linter.get_invalid_message('test', 1)
    assert invalid_message == 'Line 1: "test" should be lowercase.'

def test_get_invalid_message_capital():
    linter = KeywordLinter({'keyword_case': 'capitalize'})
    invalid_message = linter.get_invalid_message('test', 1)
    assert invalid_message == 'Line 1: "test" should be capitalized.'
