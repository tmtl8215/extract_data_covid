#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='extract_covid_data',
      version='0.0.1',
      description='Singer.io tap for extracting COVID-19 CSV data files with the GitHub API',
      author='teddy',
      classifiers=['Programming Language :: Python :: 3 :: Only'],
      py_modules=['extract_covid_data'],
      install_requires=[
          'backoff==1.8.0',
          'requests==2.23.0',
          'singer-python==5.9.0'
      ],
      entry_points='''
          [console_scripts]
          extract_covid_data=extract_covid_data:main
      ''',
      packages=find_packages(),
      package_data={
          'extract_covid_data': [
          
              'schemas/*.json'
          ]
      })
