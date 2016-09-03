#!/usr/bin/env python
"""
A template for setup.py for a Python project
"""

from setuptools import setup
from setuptools.command.test import test as TestCommand
from os import path

import io
import sys
import potato

here = path.abspath(path.dirname(__file__))


# Get the long description from the README file
def read(*filenames, **kwargs):
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)


# enables 'python setup.py test' invocation
class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errcode = pytest.main(self.test_args)
        sys.exit(errcode)


long_description = read('README.md', 'CHANGELOG.md')

setup(
    # What are you, if you don't have a name?
    name='potato',
    # Lean on existing metadata.
    version=potato.__version__,
    url='https://nope',
    license='OSL',
    author='a person',
    author_email='goodness, no',
    description='Gotta start somewhere.',
    long_description=long_description,
    platforms='any',
    tests_require=['pytest'],
    test_suite='potato.test.test_potato',
    keywords='russet idaho golden',
    packages=['potato'],
    cmdclass={'test': PyTest},

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Programming Language :: Python :: 2.7'
        'Development Status :: 3 - Alpha',
        'Intended Audience :: The Criminally Insane',
        'Topic :: Software Development :: Bad Jokes',
        'License :: OSL :: Only Sensible License',
    ],

    # List run-time dependencies here.
    install_requires=[''],

    extras_require={
        'testing': ['pytest'],
    },

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    entry_points={
        'console_scripts': [
            'potato=potato:main',
        ],
    },
)
