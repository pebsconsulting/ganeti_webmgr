#!/usr/bin/env python

from setuptools import setup

long_desc = open('README').read()

setup(name='django-muddle-users',
      version="0.5",
      description='a django app for managing users',
      long_description=long_desc,
      author='Peter Krenesky',
      author_email='peter@osuosl.org',
      maintainer="Peter Krenesky",
      maintainer_email="peter@osuosl.org",
      url='http://code.osuosl.org/projects/muddle-users',
      packages=['muddle-users'],
      include_package_data=True,
      classifiers=[
          "License :: OSI Approved :: MIT License",
          'Framework :: Django',
          'Topic :: User Management',
          ],
      )
