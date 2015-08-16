#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of LibToHttp.
# https://github.com/Utsav2/LibToHttp

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2015, Utsav Shah <ukshah2@illinois.edu>

from setuptools import setup, find_packages
from LibToHttp import __version__

tests_require = [
    'mock',
    'nose',
    'coverage',
    'yanc',
    'preggy',
    'tox',
    'ipdb',
    'coveralls',
    'sphinx',
]

setup(
    name='LibToHttp',
    version=__version__,
    description='Serves public library functions as API routes',
    long_description='''
Serves public library functions as API routes
''',
    keywords='',
    author='Utsav Shah',
    author_email='ukshah2@illinois.edu',
    url='https://github.com/Utsav2/LibToHttp',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: Unix',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: OS Independent',
    ],
    packages=find_packages(),
    include_package_data=False,
    install_requires=[
        # add your dependencies here
        # remember to use 'package-name>=x.y.z,<x.y+1.0' notation (this way you get bugfixes)
    ],
    extras_require={
        'tests': tests_require,
    },
    entry_points={
        'console_scripts': [
            # add cli scripts here in this form:
            # 'LibToHttp=LibToHttp.cli:main',
        ],
    },
)
