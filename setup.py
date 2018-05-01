#!/usr/bin/env python3

from setuptools import setup

setup(name='ultimate_ttt',
      version='1.2',
      description='Game engine for Ultimate TicTacToe games',
      author='socialgorithm',
      author_email='hello@socialgorithm.org',
      url='https://github.com/socialgorithm/ultimate-ttt-py',
      packages=['engine'],
      setup_requires=['pytest-runner'],
      tests_require=['pytest']
      )
