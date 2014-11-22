# coding: utf-8

from __future__ import unicode_literals
from __future__ import print_function
from __future__ import absolute_import
from __future__ import division
from setuptools import setup, find_packages
from django_chained_selects import get_version


with open('AUTHORS', 'rb') as fp:
    authors = ', '.join(fp.readlines())


setup(name='django-chained-select',
      version=get_version(),
      description='A django app to link two select fields together',
      author=authors,
      url='https://github.com/marazmiki/django-chained-selects',
      packages=find_packages(),
      include_package_data=True,
      requires=['django(>=1.7.1)'],
      classifiers=[
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Operating System :: OS Independent',
          'Development Status :: 4 - Beta',
          'Environment :: Web Environment',
          'Intended Audience :: Developers',
          'Framework :: Django',
          'License :: OSI Approved :: BSD License',
          'Topic :: Utilities'
      ])
