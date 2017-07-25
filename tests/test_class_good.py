
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

def test_function_good_constructor():
	# Shouldn't throw any errors
	docstringtest.processFunction(docstringtest.examples.testclass_good.ExampleGoodClass.__init__)

