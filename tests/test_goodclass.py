
import sys
import os
import importlib
import docstringtest
import docstringtest.examples.testclass_good

def test_module_good():
	# Shouldn't throw any errors
	docstringtest.processModule(docstringtest.examples.testclass_good)

def test_class_good():
	# Shouldn't throw any errors
	docstringtest.processClass(docstringtest.examples.testclass_good.ExampleGoodClass)

def test_function_good___init__():
	# Should not throw any errors
	docstringtest.processFunction(docstringtest.examples.testclass_good.ExampleGoodClass.__init__)

def test_function_good__shouldBeIgnored():
	# Should not throw any errors
	docstringtest.processFunction(docstringtest.examples.testclass_good.ExampleGoodClass._shouldBeIgnored)

def test_function_good_staticMethod():
	# Should not throw any errors
	docstringtest.processFunction(docstringtest.examples.testclass_good.ExampleGoodClass.staticMethod)

def test_function_good_staticMethodWithReturn():
	# Should not throw any errors
	docstringtest.processFunction(docstringtest.examples.testclass_good.ExampleGoodClass.staticMethodWithReturn)

def test_function_good_basicMethod():
	# Should not throw any errors
	docstringtest.processFunction(docstringtest.examples.testclass_good.ExampleGoodClass.basicMethod)

def test_function_good_basicMethodWithReturn():
	# Should not throw any errors
	docstringtest.processFunction(docstringtest.examples.testclass_good.ExampleGoodClass.basicMethodWithReturn)

def test_function_good_basicMethodWithYield():
	# Should not throw any errors
	docstringtest.processFunction(docstringtest.examples.testclass_good.ExampleGoodClass.basicMethodWithYield)

def test_function_good_staticMethodNoVariables():
	# Should not throw any errors
	docstringtest.processFunction(docstringtest.examples.testclass_good.ExampleGoodClass.staticMethodNoVariables)

def test_function_good_staticMethodNoVariablesWithReturn():
	# Should not throw any errors
	docstringtest.processFunction(docstringtest.examples.testclass_good.ExampleGoodClass.staticMethodNoVariablesWithReturn)

def test_function_good_staticMethodNoVariablesWithYield():
	# Should not throw any errors
	docstringtest.processFunction(docstringtest.examples.testclass_good.ExampleGoodClass.staticMethodNoVariablesWithYield)

