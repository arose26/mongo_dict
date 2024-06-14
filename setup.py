#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# MIT License
#
# Copyright (c) 2024 Alan Rose
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
__author__ = 'Alan Rose'


def readme():
	return 'readme'

import sys
if sys.version_info < (3, 4, 1):
    sys.exit('Python < 3.4.1 is not supported!')

from setuptools import setup
# Define the package metadata
name = 'mongo_dict'
version = 0.0.3
description = 'Use mongo through python dicts'
author = 'Alan Rose'
author_email = 'your_email@example.com'
url = 'https://github.com/arose26/mongo_dict'

# Define the dependencies
install_requires = [
    'pymongo'
]

# Define the package structure
packages = ['mongo_dict']



# Define the setup
setup(
    name=name,
    version=version,
    description=description,
    author=author,
    author_email=author_email,
    url=url,
    packages=packages,
    install_requires=install_requires,
)
