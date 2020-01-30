from setuptools import setup

import os
import sys

from setuptools import setup, find_packages, find_namespace_packages

# sys.dont_write_bytecode = True

setup(
    name='something',
    packages=find_namespace_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
)

