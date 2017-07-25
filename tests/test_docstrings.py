
import sys
import os
import importlib
import docstringtest

def addDataDirToPath():
	thisDir = os.path.dirname(os.path.realpath(__file__))
	dataDir = os.path.join(thisDir,'data')
	sys.path.append(dataDir)
	return dataDir

def test_docstring_constructor():
	addDataDirToPath()
	mod = importlib.import_module('testclass_good')

	expected = [':param self: description',
		':param varA: description',
		':param varB: description',
		':param varC: description',
		':type self: type description',
		':type varA: type description',
		':type varB: type description',
		':type varC: type description']
	docstring = docstringtest.generateDocstring(mod.TestClass.__init__)

	assert docstring == "\n".join(expected)


def test_docstring_method():
	addDataDirToPath()
	mod = importlib.import_module('testclass_good')

	expected = [':param self: description',
		':param varA: description',
		':param varB: description',
		':type self: type description',
		':type varA: type description',
		':type varB: type description']
	docstring = docstringtest.generateDocstring(mod.TestClass.basicMethod)

	assert docstring == "\n".join(expected)

def test_docstring_withReturn():
	addDataDirToPath()
	mod = importlib.import_module('testclass_good')

	expected = [':param self: description',
		':param varA: description',
		':param varB: description',
		':type self: type description',
		':type varA: type description',
		':type varB: type description',
		':return: return description',
		':rtype: the return type description']
	docstring = docstringtest.generateDocstring(mod.TestClass.basicMethodWithReturn)

	assert docstring == "\n".join(expected)

def test_docstring_withYield():
	addDataDirToPath()
	mod = importlib.import_module('testclass_good')

	expected = [':param self: description',
		':param varA: description',
		':param varB: description',
		':type self: type description',
		':type varA: type description',
		':type varB: type description',
		':return: return description',
		':rtype: the return type description']
	docstring = docstringtest.generateDocstring(mod.TestClass.basicMethodWithYield)

	assert docstring == "\n".join(expected)
