
import docstringtest
import docstringtest.examples.goodfunctions

def test_module():
	# Shouldn't return any errors
	docstringtest.testModule(docstringtest.examples.goodfunctions)

def test_testfunction():
	# Shouldn't return any errors
	docstringtest.testFunction(docstringtest.examples.goodfunctions.testfunction)

def test_testfunctionWithReturn():
	# Shouldn't return any errors
	docstringtest.testFunction(docstringtest.examples.goodfunctions.testfunctionWithReturn)

def test__shouldBeSkipped():
	# Shouldn't return any errors
	docstringtest.testFunction(docstringtest.examples.goodfunctions._shouldBeSkipped)

def test__shouldBeSkippedWithReturn():
	# Shouldn't return any errors
	docstringtest.testFunction(docstringtest.examples.goodfunctions._shouldBeSkippedWithReturn)

