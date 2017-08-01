
import os
import inspect

class DocstringTestError(RuntimeError):
	def __init__(self, message, filename, funcName):
		super(DocstringTestError, self).__init__(message)
		self.message = message
		self.funcName = funcName
		self.filename = os.path.abspath(filename)
	
	def __str__(self):
		return "%s for function %s in file %s" % (self.message,self.funcName,self.filename)

def codeReturnsSomething(func):
	sourceCode = inspect.getsource(func).split('\n')
	for line in sourceCode:
		tokens = line.strip().split()
		if len(tokens) >= 2 and (tokens[0] == 'return' or tokens[0] == 'yield'):
			return True
	return False

def generateDocstring(func):
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

def generateAllDocstrings(c):
	assert inspect.isclass(c)
	output = []
	for name,obj in inspect.getmembers(c):
		if inspect.ismethod(obj) or inspect.isfunction(obj):
			output.append("-"*30)
			output.append(name)
			output.append('"""')
			output.append(generateDocstring(obj))
			output.append('"""')
	return "\n".join(output)

def processFunction(func):
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


def processClass(c):
	for name,obj in inspect.getmembers(c):
		if inspect.ismethod(obj) or inspect.isfunction(obj):
			processFunction(obj)

def processModule(m):
	for name,obj in inspect.getmembers(m):
		if inspect.isclass(obj):
			processClass(obj)
		elif inspect.isfunction(obj):
			processFunction(obj)
