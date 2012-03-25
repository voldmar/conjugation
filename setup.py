#!/usr/bin/env python

from distutils.core import setup

setup(name='conjugation',
      version='1.0.4',
      description='Spanish verb conjugation library',
      author='Vladimir Epifanov',
      author_email='voldmar@voldmar.ru',
      url='https://github.com/voldmar/conjugation',
      packages=['conjugation'],
      package_dir={'conjugation': 'conjugation'},
      package_data={'conjugation': ['irregular_verbs.txt']},
)
