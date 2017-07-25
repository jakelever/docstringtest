
import sys
import os
import importlib
import docstringtest
from docstringtest.examples.testclass_good import ExampleGoodClass

def test_docstring_constructor():
	func = ExampleGoodClass.__init__
	expected = [':param self: description',
		':param varA: description',
		':param varB: description',
		':param varC: description',
		':type self: type description',
		':type varA: type description',
		':type varB: type description',
		':type varC: type description']
	docstring = docstringtest.generateDocstring(func)

	assert docstring == "\n".join(expected)


def test_docstring_method():
	func = ExampleGoodClass.basicMethod
	expected = [':param self: description',
		':param varA: description',
		':param varB: description',
		':type self: type description',
		':type varA: type description',
		':type varB: type description']
	docstring = docstringtest.generateDocstring(func)

	assert docstring == "\n".join(expected)

def test_docstring_withReturn():
	func = ExampleGoodClass.basicMethodWithReturn
	expected = [':param self: description',
		':param varA: description',
		':param varB: description',
		':type self: type description',
		':type varA: type description',
		':type varB: type description',
		':return: return description',
		':rtype: the return type description']
	docstring = docstringtest.generateDocstring(func)

	assert docstring == "\n".join(expected)

def test_docstring_withYield():
	func = ExampleGoodClass.basicMethodWithYield
	expected = [':param self: description',
		':param varA: description',
		':param varB: description',
		':type self: type description',
		':type varA: type description',
		':type varB: type description',
		':return: return description',
		':rtype: the return type description']
	docstring = docstringtest.generateDocstring(func)

	assert docstring == "\n".join(expected)
