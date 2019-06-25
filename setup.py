#!/usr/bin/env python

import os

from setuptools import find_packages
from setuptools import setup

setup(name = 'mkpypkg',
      description = 'Initializes an empty Python package to my own tastes.',
      author = 'C. Gosmeyer',
      url = 'https://github.com/cgosmeyer/mkpypkg',
      packages = find_packages())

if not os.path.isfile('mkpypkg_config.py'):
	open('mkpypkg_config.py', 'a').close()
	print('created mkpypkg_config.py')
else:
	print('mkpypkg_config.py already exists')