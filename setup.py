#!/usr/bin/env python
#coding:utf-8
# Author:  mozman
# Purpose: setup
# Created: 14.03.2010
# Copyright (C) 2010, Manfred Moitzi
# License: GPLv3

import os
from distutils.core import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(name='dxfwrite',
    version='0.1.0',
    description='library to create DXF R12 drawings',
    author='mozman',
    author_email='mozman@gmx.at',
    packages=['dxfwrite', 'tests'],
    long_description=read('README'),
    classifiers=[
    "Development Status :: 3 - Alpha",
    "License :: OSI Approved :: GNU General Public License (GPL)",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 2.6",
    "Intended Audience :: Developers",
    "Topic :: Multimedia :: Graphics :: 3D Modeling",
    ]
     )
