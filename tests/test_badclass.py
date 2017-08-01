
import os
import pytest
import docstringtest
import docstringtest.examples.badclass

def test_module_bad():
	with pytest.raises(docstringtest.DocstringTestError) as excinfo:
		docstringtest.processModule(docstringtest.examples.badclass)
	print(excinfo.value.message,excinfo.value.funcName)
	assert excinfo.value.message == "Missing docstring"
	assert excinfo.value.funcName == "__init__"
	assert os.path.basename(excinfo.value.filename) == 'badclass.py'

def test_class_bad():
	with pytest.raises(docstringtest.DocstringTestError) as excinfo:
		docstringtest.processClass(docstringtest.examples.badclass.BadClass)
	assert excinfo.value.message == "Missing docstring"
	assert excinfo.value.funcName == "__init__"
	assert os.path.basename(excinfo.value.filename) == 'badclass.py'

def test_function_bad___init__():
	with pytest.raises(docstringtest.DocstringTestError) as excinfo:
		docstringtest.processFunction(docstringtest.examples.badclass.BadClass.__init__)
	assert excinfo.value.message == "Missing docstring"
	assert excinfo.value.funcName == "__init__"
	assert os.path.basename(excinfo.value.filename) == 'badclass.py'

def test_function_bad__shouldBeIgnored():
	# Shouldn't throw any errors
	docstringtest.processFunction(docstringtest.examples.badclass.BadClass._shouldBeIgnored)

def test_function_bad_staticMethod():
	with pytest.raises(docstringtest.DocstringTestError) as excinfo:
		docstringtest.processFunction(docstringtest.examples.badclass.BadClass.staticMethod)
	assert excinfo.value.message == "Missing ':type varA:' in docstring"
	assert excinfo.value.funcName == "staticMethod"
	assert os.path.basename(excinfo.value.filename) == 'badclass.py'

def test_function_bad_staticMethodWithReturn():
	with pytest.raises(docstringtest.DocstringTestError) as excinfo:
		docstringtest.processFunction(docstringtest.examples.badclass.BadClass.staticMethodWithReturn)
	assert excinfo.value.message == "Missing ':return:' in docstring"
	assert excinfo.value.funcName == "staticMethodWithReturn"
	assert os.path.basename(excinfo.value.filename) == 'badclass.py'

def test_function_bad_basicMethod():
	with pytest.raises(docstringtest.DocstringTestError) as excinfo:
		docstringtest.processFunction(docstringtest.examples.badclass.BadClass.basicMethod)
	assert excinfo.value.message == "Missing ':param self:' in docstring"
	assert excinfo.value.funcName == "basicMethod"
	assert os.path.basename(excinfo.value.filename) == 'badclass.py'

def test_function_bad_basicMethodWithReturn():
	with pytest.raises(docstringtest.DocstringTestError) as excinfo:
		docstringtest.processFunction(docstringtest.examples.badclass.BadClass.basicMethodWithReturn)
	assert excinfo.value.message == "Missing ':param varB:' in docstring"
	assert excinfo.value.funcName == "basicMethodWithReturn"
	assert os.path.basename(excinfo.value.filename) == 'badclass.py'

def test_function_bad_basicMethodWithYield():
	with pytest.raises(docstringtest.DocstringTestError) as excinfo:
		docstringtest.processFunction(docstringtest.examples.badclass.BadClass.basicMethodWithYield)
	assert excinfo.value.message == "Missing ':return:' in docstring"
	assert excinfo.value.funcName == "basicMethodWithYield"
	assert os.path.basename(excinfo.value.filename) == 'badclass.py'

def test_function_bad_staticMethodNoVariables():
	with pytest.raises(docstringtest.DocstringTestError) as excinfo:
		docstringtest.processFunction(docstringtest.examples.badclass.BadClass.staticMethodNoVariables)
	assert excinfo.value.message == "Unexpected ':return: return description' in docstring"
	assert excinfo.value.funcName == "staticMethodNoVariables"
	assert os.path.basename(excinfo.value.filename) == 'badclass.py'

def test_function_bad_staticMethodNoVariablesWithReturn():
	with pytest.raises(docstringtest.DocstringTestError) as excinfo:
		docstringtest.processFunction(docstringtest.examples.badclass.BadClass.staticMethodNoVariablesWithReturn)
	assert excinfo.value.message == "Missing description of function in docstring"
	assert excinfo.value.funcName == "staticMethodNoVariablesWithReturn"
	assert os.path.basename(excinfo.value.filename) == 'badclass.py'

def test_function_bad_staticMethodNoVariablesWithYield():
	with pytest.raises(docstringtest.DocstringTestError) as excinfo:
		docstringtest.processFunction(docstringtest.examples.badclass.BadClass.staticMethodNoVariablesWithYield)
	assert excinfo.value.message == "Missing docstring"
	assert excinfo.value.funcName == "staticMethodNoVariablesWithYield"
	assert os.path.basename(excinfo.value.filename) == 'badclass.py'


if __name__ == '__main__':
	test_function_bad___init__()
