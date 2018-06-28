"""Packaging settings."""


from codecs import open
from os.path import abspath, dirname, join
from subprocess import call

from setuptools import Command, find_packages, setup

LONG_DESCRIPTION = """
lintthesql is a SQL linter and formatter.
"""

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

print(requirements)

setup(
    name = 'lintthesql',
    version = '1.0.0',
    description = 'A sql linter and formatter',
    long_description = LONG_DESCRIPTION,
    url = '',
    author = 'Garrett and David',
    author_email = '',
    license = 'MIT',
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Utilities',
        'License :: Public Domain',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3 :: Only',
    ],
    keywords = 'cli, lint, formatter, sql',
    packages = find_packages(exclude=['docs', 'tests*', 'examples']),
    install_requires = ['sqlparse','PyYaml'],
    dependency_links = ['git+https://github.com/So-Cool/nyanbar/tarball/master@egg=nyanbar'],
    entry_points = {
        'console_scripts': [
            'lintthesql=lintthesql',
        ],
    },
)
