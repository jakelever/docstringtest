
import sys
import os
import importlib
import docstringtest
import docstringtest.examples.goodclass

def test_module_good():
	# Shouldn't throw any errors
	docstringtest.testModule(docstringtest.examples.goodclass)

def test_class_good():
	# Shouldn't throw any errors
	docstringtest.testClass(docstringtest.examples.goodclass.GoodClass)

def test_function_good___init__():
	# Should not throw any errors
	docstringtest.testFunction(docstringtest.examples.goodclass.GoodClass.__init__)

def test_function_good__shouldBeIgnored():
	# Should not throw any errors
	docstringtest.testFunction(docstringtest.examples.goodclass.GoodClass._shouldBeIgnored)

def test_function_good_staticMethod():
	# Should not throw any errors
	docstringtest.testFunction(docstringtest.examples.goodclass.GoodClass.staticMethod)

def test_function_good_staticMethodWithReturn():
	# Should not throw any errors
	docstringtest.testFunction(docstringtest.examples.goodclass.GoodClass.staticMethodWithReturn)

def test_function_good_basicMethod():
	# Should not throw any errors
	docstringtest.testFunction(docstringtest.examples.goodclass.GoodClass.basicMethod)

def test_function_good_basicMethodWithReturn():
	# Should not throw any errors
	docstringtest.testFunction(docstringtest.examples.goodclass.GoodClass.basicMethodWithReturn)

def test_function_good_basicMethodWithYield():
	# Should not throw any errors
	docstringtest.testFunction(docstringtest.examples.goodclass.GoodClass.basicMethodWithYield)

def test_function_good_staticMethodNoVariables():
	# Should not throw any errors
	docstringtest.testFunction(docstringtest.examples.goodclass.GoodClass.staticMethodNoVariables)

def test_function_good_staticMethodNoVariablesWithReturn():
	# Should not throw any errors
	docstringtest.testFunction(docstringtest.examples.goodclass.GoodClass.staticMethodNoVariablesWithReturn)

def test_function_good_staticMethodNoVariablesWithYield():
	# Should not throw any errors
	docstringtest.testFunction(docstringtest.examples.goodclass.GoodClass.staticMethodNoVariablesWithYield)

