
import os
import inspect

class DocstringTestError(RuntimeError):
	"""
	Special Error for Docstring test failures where an appropriate docstring is not found for a function/method
	"""

	def __init__(self, message, filename, funcName):
		"""
		Constructor for the DocstringTestError class

		:param message: Message for the specific error
		:param filename: Filename for the Python code that contains the function/method
		:param funcName: Name of the function which has an docstring error
		:type message: str
		:type filename: str
		:type funcName: str
		"""

		super(DocstringTestError, self).__init__(message)
		self.message = message
		self.funcName = funcName
		self.filename = os.path.abspath(filename)
	
	def __str__(self):
		"""
		Get a string representation of the error
		
		:return: String representation of this error including the message, function name and filename
		:rtype: str
		"""
		return "%s for function %s in file %s" % (self.message,self.funcName,self.filename)

def codeReturnsSomething(func):
	"""
	Checks whether a function/method appears to have a return statement that returns data. It simply examines the code for the function/method looking for a return call.

	:param func: Function to check
	:type func: function/method
	:return: Whether the function/method
	:rtype: bool
	"""

	sourceCode = inspect.getsource(func).split('\n')
	for line in sourceCode:
		tokens = line.strip().split()
		if len(tokens) >= 2 and (tokens[0] == 'return' or tokens[0] == 'yield'):
			return True
	return False

def generateAllDocstrings(c):
	"""
	Generate skeleton docstrings for all functions/methods in a module or class

	:param c: Module or class to generate docstrings for
	:type c: module/class
	:return: All docstrings for functions/methods
	:rtype: str
	"""

	assert inspect.isclass(c) or inspect.ismodule(c)
	output = []
	for name,obj in inspect.getmembers(c):
		if inspect.ismethod(obj) or inspect.isfunction(obj):
			output.append("-"*30)
			output.append(name)
			output.append('"""')
			output.append(generateDocstring(obj))
			output.append('"""')
	return "\n".join(output)

def generateDocstring(func):
	"""
	Generates a skeleton docstring (to be filled in) for a function/method

	:param func: Function/method that docstring should be generated for
	:type func: function/method
	:return: Skeleton docstring for function/method
	:rtype: str
	"""

	assert inspect.isfunction(func) or inspect.ismethod(func)

	methodArgs = func.__code__.co_varnames[:func.__code__.co_argcount]
	
	params = [ ":param %s: description" % methodArg for methodArg in methodArgs ]
	types = [ ":type %s: type description" % methodArg for methodArg in methodArgs ]

	# Remove first parameter if name is self (like a method of a class)
	if len(methodArgs) >= 1 and methodArgs[0] == 'self':
		params = params[1:]
		types = types[1:]

	returns = []
	if codeReturnsSomething(func):
		returns = [":return: return description",":rtype: the return type description"]

	txt = "\n".join(params + types + returns)

	return txt


def testFunction(func):
	"""
	Test a function/method to see if the necessary docstring is included. Will check for line describing each parameter and its type. Will also expected at least one line with description of function.

	:param func: Function/method to test
	:type func: function/method
	"""

	funcName = func.__code__.co_name

	# Skip methods that start with '_' except for constructors
	if funcName.startswith('_') and not funcName == '__init__':
		return

	funcFilename = func.__code__.co_filename
	methodArgs = func.__code__.co_varnames[:func.__code__.co_argcount]
	
	params = [ ":param %s:" % methodArg for methodArg in methodArgs ]
	types = [ ":type %s:" % methodArg for methodArg in methodArgs ]
	
	# Remove first parameter if name is self (like a method of a class)
	if len(methodArgs) >= 1 and methodArgs[0] == 'self':
		params = params[1:]
		types = types[1:]

	returns = []
	if codeReturnsSomething(func):
		returns = [":return:",":rtype:"]

	expected = params + types + returns

	if func.__doc__ is None:
		raise DocstringTestError("Missing docstring",funcFilename,funcName)

	docstring = func.__doc__.split('\n')
	docstring = [ line.strip() for line in docstring ]
	docstring = [ line for line in docstring if line ]

	docstringWithParams = [ line for line in docstring if line.startswith(':param') or line.startswith(':type') or line.startswith(':return: ') or line.startswith(':rtype: ') ]

	for i in range(max(len(expected),len(docstringWithParams))):
		if i >= len(docstringWithParams):
			raise DocstringTestError("Missing '%s' in docstring" % expected[i],funcFilename,funcName)
		elif i >= len(expected):
			raise DocstringTestError("Unexpected '%s' in docstring" % docstringWithParams[i],funcFilename,funcName)
		elif not docstringWithParams[i].startswith(expected[i]):
			raise DocstringTestError("Missing '%s' in docstring" % expected[i],funcFilename,funcName)

	# If we have exactly the parameter info and nothing else, then we're missing a description (of some length) about what the function does
	if len(expected) == len(docstring):
		raise DocstringTestError("Missing description of function in docstring" ,funcFilename,funcName)


def testClass(c):
	"""
	Test all the docstrings for methods in a class

	:param c: Class to test
	:type c: class
	"""

	for name,obj in inspect.getmembers(c):
		if inspect.ismethod(obj) or inspect.isfunction(obj):
			testFunction(obj)

def testModule(m):
	"""
	Test all the docstrings for classes/functions/methods in a module

	:param m: Module to test
	:type m: module
	"""

	for name,obj in inspect.getmembers(m):
		if inspect.isclass(obj):
			testClass(obj)
		elif inspect.isfunction(obj):
			testFunction(obj)

