
import sys
import os
import importlib
import docstringtest

def addDataDirToPath():
	thisDir = os.path.dirname(os.path.realpath(__file__))
	dataDir = os.path.join(thisDir,'data')
	sys.path.append(dataDir)
	return dataDir

def test_module_good():
	addDataDirToPath()
	mod = importlib.import_module('testclass_good')

	# Shouldn't throw any errors
	docstringtest.processModule(mod)

def test_class_good():
	addDataDirToPath()
	mod = importlib.import_module('testclass_good')

	# Shouldn't throw any errors
	docstringtest.processClass(mod.TestClass)

def test_function_good_constructor():
	addDataDirToPath()
	mod = importlib.import_module('testclass_good')

	# Shouldn't throw any errors
	docstringtest.processFunction(mod.TestClass.__init__)

