
import sys
import os
import importlib
import docstringtest
from docstringtest.examples.goodclass import GoodClass

def test_docstring_constructor():
	func = GoodClass.__init__
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
	func = GoodClass.basicMethod
	expected = [':param self: description',
		':param varA: description',
		':param varB: description',
		':type self: type description',
		':type varA: type description',
		':type varB: type description']
	docstring = docstringtest.generateDocstring(func)

	assert docstring == "\n".join(expected)

def test_docstring_withReturn():
	func = GoodClass.basicMethodWithReturn
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
	func = GoodClass.basicMethodWithYield
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
