
import docstringtest.examples.goodfunctions as goodfuncs
from docstringtest.examples.goodclass import GoodClass
from docstringtest.examples.badclass import BadClass

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
	goodObj = GoodClass(None,None,None)
	goodObj._shouldBeIgnored(None, None)
	goodObj.basicMethod(None,None)
	assert goodObj.basicMethodWithReturn(None,None) == 1
	for i,val in enumerate(goodObj.basicMethodWithYield(None,None)):
		assert i==val

	GoodClass.staticMethodNoVariables()
	assert GoodClass.staticMethodNoVariablesWithReturn() == 1
	for i,val in enumerate(GoodClass.staticMethodNoVariablesWithYield()):
		assert i==val
	GoodClass.staticMethod(None)
	assert GoodClass.staticMethodWithReturn(None) == 1
	
	# Test the class that doesn't have docstring issues
	badObj = BadClass(None,None,None)
	badObj._shouldBeIgnored(None, None)
	badObj.basicMethod(None,None)
	assert badObj.basicMethodWithReturn(None,None) == 1
	for i,val in enumerate(badObj.basicMethodWithYield(None,None)):
		assert i==val

	BadClass.staticMethodNoVariables()
	assert BadClass.staticMethodNoVariablesWithReturn() == 1
	for i,val in enumerate(BadClass.staticMethodNoVariablesWithYield()):
		assert i==val
	BadClass.staticMethod(None)
	assert BadClass.staticMethodWithReturn(None) == 1
