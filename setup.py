#!/usr/bin/env python
# coding=utf-8

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

APP_NAME = 'cloudant'
VERSION = '0.1.0'

# Publish Helper.
if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

settings = {}

settings.update(
    name=APP_NAME,
    version=VERSION,
    author='Dustin Collins',
    author_email='dustinrcollins@gmail.com',
    packages=['cloudant'],
    package_data={'cloudant':['*.md', '*.txt']},
    url='https://github.com/dustinmm80/cloudant',
    license='MIT',
    description='Python library to use the CloudAnt API',
    long_description=open('README.md').read(),
    zip_safe=False,
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3'
    ],
    test_suite='nose.collector',
    tests_require=['nose'],
    install_requires=open('requirements.txt').readlines(),
)

setup(**settings)