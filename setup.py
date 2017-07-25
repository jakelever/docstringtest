#!/usr/bin/env python

from distutils.core import setup

setup(name='docstringtest',
	version='1.0',
	description='Procedure to check for valid docstrings',
	author='Jake Lever',
	author_email='jake.lever@gmail.com',
	url='https://github.com/jakelever/docstringtest',
	scripts=['scripts/docstringtest'],
	license='MIT',
	packages=['kindred'],
	install_requires=[],
	include_package_data=True,
	)
