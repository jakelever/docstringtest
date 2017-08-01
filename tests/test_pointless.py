
import docstringtest.examples.testfunctions_good as goodfuncs
from docstringtest.examples.testclass_good import ExampleGoodClass
from docstringtest.examples.testclass_bad import ExampleBadClass

def test_pointless():
	"""
	This test just runs all the example code and is purely for coverage purposes
	"""

	# Test the functions that don't have docstring issues
	goodfuncs.testfunction(None, None)
	assert goodfuncs.testfunctionWithReturn(None, None, None) == 1
	goodfuncs._shouldBeSkipped(None, None)
	assert goodfuncs._shouldBeSkippedWithReturn(None, None) == 1

	# Test the class that doesn't have docstring issues
	goodObj = ExampleGoodClass(None,None,None)
	goodObj._shouldBeIgnored(None, None)
	goodObj.basicMethod(None,None)
	assert goodObj.basicMethodWithReturn(None,None) == 1
	for i,val in enumerate(goodObj.basicMethodWithYield(None,None)):
		assert i==val

	ExampleGoodClass.staticMethodNoVariables()
	assert ExampleGoodClass.staticMethodNoVariablesWithReturn() == 1
	for i,val in enumerate(ExampleGoodClass.staticMethodNoVariablesWithYield()):
		assert i==val
	ExampleGoodClass.staticMethod(None)
	assert ExampleGoodClass.staticMethodWithReturn(None) == 1
	
	# Test the class that doesn't have docstring issues
	badObj = ExampleBadClass(None,None,None)
	badObj._shouldBeIgnored(None, None)
	badObj.basicMethod(None,None)
	assert badObj.basicMethodWithReturn(None,None) == 1
	for i,val in enumerate(badObj.basicMethodWithYield(None,None)):
		assert i==val

	ExampleBadClass.staticMethodNoVariables()
	assert ExampleBadClass.staticMethodNoVariablesWithReturn() == 1
	for i,val in enumerate(ExampleBadClass.staticMethodNoVariablesWithYield()):
		assert i==val
	ExampleBadClass.staticMethod(None)
	assert ExampleBadClass.staticMethodWithReturn(None) == 1
