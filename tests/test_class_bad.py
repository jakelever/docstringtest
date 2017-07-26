
import os
import pytest
import docstringtest
import docstringtest.examples.testclass_bad

def test_module_bad():
	with pytest.raises(docstringtest.DocstringTestError) as excinfo:
		docstringtest.processModule(docstringtest.examples.testclass_bad)
	assert excinfo.value.message == "Expected docstring"
	assert excinfo.value.funcName == "__init__"
	assert os.path.basename(excinfo.value.filename) == 'testclass_bad.py'

def test_class_bad():
	with pytest.raises(docstringtest.DocstringTestError) as excinfo:
		docstringtest.processClass(docstringtest.examples.testclass_bad.ExampleBadClass)
	assert excinfo.value.message == "Expected docstring"
	assert excinfo.value.funcName == "__init__"
	assert os.path.basename(excinfo.value.filename) == 'testclass_bad.py'

def test_function_bad___init__():
	with pytest.raises(docstringtest.DocstringTestError) as excinfo:
		docstringtest.processFunction(docstringtest.examples.testclass_bad.ExampleBadClass.__init__)
	assert excinfo.value.message == "Expected docstring"
	assert excinfo.value.funcName == "__init__"
	assert os.path.basename(excinfo.value.filename) == 'testclass_bad.py'

def test_function_bad__shouldBeIgnored():
	# Shouldn't throw any errors
	docstringtest.processFunction(docstringtest.examples.testclass_bad.ExampleBadClass._shouldBeIgnored)

def test_function_bad_staticMethod():
	with pytest.raises(docstringtest.DocstringTestError) as excinfo:
		docstringtest.processFunction(docstringtest.examples.testclass_bad.ExampleBadClass.staticMethod)
	assert excinfo.value.message == "Expected ':type varA:' in docstring"
	assert excinfo.value.funcName == "staticMethod"
	assert os.path.basename(excinfo.value.filename) == 'testclass_bad.py'

def test_function_bad_staticMethodWithReturn():
	with pytest.raises(docstringtest.DocstringTestError) as excinfo:
		docstringtest.processFunction(docstringtest.examples.testclass_bad.ExampleBadClass.staticMethodWithReturn)
	assert excinfo.value.message == "Expected ':return:' in docstring"
	assert excinfo.value.funcName == "staticMethodWithReturn"
	assert os.path.basename(excinfo.value.filename) == 'testclass_bad.py'

def test_function_bad_basicMethod():
	with pytest.raises(docstringtest.DocstringTestError) as excinfo:
		docstringtest.processFunction(docstringtest.examples.testclass_bad.ExampleBadClass.basicMethod)
	assert excinfo.value.message == "Expected ':param self:' in docstring"
	assert excinfo.value.funcName == "basicMethod"
	assert os.path.basename(excinfo.value.filename) == 'testclass_bad.py'

def test_function_bad_basicMethodWithReturn():
	with pytest.raises(docstringtest.DocstringTestError) as excinfo:
		docstringtest.processFunction(docstringtest.examples.testclass_bad.ExampleBadClass.basicMethodWithReturn)
	assert excinfo.value.message == "Expected ':param varB:' in docstring"
	assert excinfo.value.funcName == "basicMethodWithReturn"
	assert os.path.basename(excinfo.value.filename) == 'testclass_bad.py'

def test_function_bad_basicMethodWithYield():
	with pytest.raises(docstringtest.DocstringTestError) as excinfo:
		docstringtest.processFunction(docstringtest.examples.testclass_bad.ExampleBadClass.basicMethodWithYield)
	assert excinfo.value.message == "Expected ':return:' in docstring"
	assert excinfo.value.funcName == "basicMethodWithYield"
	assert os.path.basename(excinfo.value.filename) == 'testclass_bad.py'

def test_function_bad_staticMethodNoVariables():
	with pytest.raises(docstringtest.DocstringTestError) as excinfo:
		docstringtest.processFunction(docstringtest.examples.testclass_bad.ExampleBadClass.staticMethodNoVariables)
	assert excinfo.value.message == "Unexpected ':return: return description' in docstring"
	assert excinfo.value.funcName == "staticMethodNoVariables"
	assert os.path.basename(excinfo.value.filename) == 'testclass_bad.py'

def test_function_bad_staticMethodNoVariablesWithReturn():
	with pytest.raises(docstringtest.DocstringTestError) as excinfo:
		docstringtest.processFunction(docstringtest.examples.testclass_bad.ExampleBadClass.staticMethodNoVariablesWithReturn)
	assert excinfo.value.message == "Expected description of function in docstring"
	assert excinfo.value.funcName == "staticMethodNoVariablesWithReturn"
	assert os.path.basename(excinfo.value.filename) == 'testclass_bad.py'

def test_function_bad_staticMethodNoVariablesWithYield():
	with pytest.raises(docstringtest.DocstringTestError) as excinfo:
		docstringtest.processFunction(docstringtest.examples.testclass_bad.ExampleBadClass.staticMethodNoVariablesWithYield)
	assert excinfo.value.message == "Expected docstring"
	assert excinfo.value.funcName == "staticMethodNoVariablesWithYield"
	assert os.path.basename(excinfo.value.filename) == 'testclass_bad.py'

