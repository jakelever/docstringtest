#!/usr/bin/env python

import argparse
import importlib


if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='')
	parser.add_argument('--package', type=str, required=True, help='Name of package to check')
	args = parser.parse_args()

	packageName = args.package
	mod = importlib.import_module(packageName)

	#processModule(mod)

	import kindred
	processClass(kindred.RelationClassifier)
	#print dir(mod.__init__)

	#for x in dir(mod):
	#	print x
	#	print dir(x)
	#	print '-'*30
