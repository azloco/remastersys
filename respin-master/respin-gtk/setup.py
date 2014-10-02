#!/usr/bin/env python
# -*- coding:utf-8 -*-

import glob
from setuptools import setup, find_packages

setup(name = 'respin-gtk',
    version = '1.0',
    description='Ubuntu and variant system remaster. This is the alternate gtk gui for respin written in pygtk.',
    author='Tony Brijeski', 
    author_email='tb6517@yahoo.com',
    url='http://www.linuxrespin.org',
    scripts=['respin-gtk'],
    packages = find_packages(),
    data_files = [
        ('share/respin-gtk/ui/', glob.glob('data/ui/*.glade')),
        ('share/respin-gtk/pixmaps/', glob.glob('data/pixmaps/*.png')),
        ('bin/', glob.glob('data/scripts/plymouth-preview')),
        ('share/man/man1/', glob.glob('man/man1/*.1')),
    ],
    license='GNU GPL',
    platforms='linux',
)
