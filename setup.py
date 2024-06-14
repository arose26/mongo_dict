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
import sys
from setuptools import setup, setuptools
from mongo_dict import __version__


__author__ = 'Alan Rose'


def readme():
    with open('README.rst', encoding="UTF-8") as f:
        return f.read()


if sys.version_info < (3, 4, 1):
    sys.exit('Python < 3.4.1 is not supported!')


setup(name='mongo_dict',
      version=__version__,
      description='Python Mongo-Dict, a dictionary-like class automatically stored in mongo, with query capabilities.',
      long_description=readme(),
      url='http://github.com/arose26/mongo_dict',
      author='Alan Rose',
      author_email='',
      license='MIT',
      packages=setuptools.find_packages(),
      install_requires=[
          "pymongo"
      ],
      classifiers=[
          'Environment :: Console',
          'Intended Audience :: Developers',
          'Intended Audience :: Education',
          'Intended Audience :: Science/Research',
          'Natural Language :: English',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
      ],
      test_suite='nose.collector',
      tests_require=['nose'],
      include_package_data=True,
      keywords="",
      zip_safe=False)