#  -*- coding: utf-8 -*-
"""
Setup tools script for Red Badger Code Challenge application.
"""

import os

from setuptools import setup, find_packages

def required(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read().split('\n')

config = {
    "name" : "robots",
    "version" : "19.04.0",
    "namespace_packages" : [ ],
    "packages" : find_packages(exclude=[
                                         "*.tests", "*.tests.*", "tests.*", "tests",
                                         "*.ez_setup", "*.ez_setup.*", "ez_setup.*", "ez_setup",
                                         "*.examples", "*.examples.*", "examples.*", "examples",
                                       ]),
    "include_package_data" : True,
    "package_data" : {
                       "" : [ ],
                     },
    "data_files" : [],
    "scripts" : [ ],
    "entry_points" : { },
    "install_requires" : [  required('requirements.txt') ],
    "tests_require" : [ required('requirements-for-test.txt') ],
    "test_suite" : 'pytest',
    "zip_safe" : False,

    # Metadata for upload to PyPI
    "author" : 'Matthew Green',
    "author_email" : "matthew@newedgeengineering.com",
    "description" : "A command line application that reads a data file to control virtual robots.",
    "long_description" : """ """,
    "classifiers" : [
                        'Environment :: Console',
                        'Intended Audience :: Developers',
                        'License :: OSI Approved :: MIT License',
                        'Programming Language :: Python',
                    ],
    "license" : "",
    "keywords" : "",
    "url" : "",
}

setup(**config)
