
import inspect

class DocstringTestError(RuntimeError):
	def __init__(self, message, filename, funcName=None):
		super(DocstringTestError, self).__init__(message)
		self.message = message
		self.funcName = funcName
		self.filename = filename
	
	def __str__(self):
		if self.funcName is None:
			return "%s in file %s" % (self.message,self.filename)
		else:	
			return "%s for function %s in file %s" % (self.message,self.funcName,self.filename)

def codeReturnsSomething(func):
	sourceCode = inspect.getsource(func).split('\n')
	for line in sourceCode:
		tokens = line.strip().split()
		if len(tokens) >= 2 and (tokens[0] == 'return' or tokens[0] == 'yield'):
			return True
	return False

def generateDocstring(func):
	methodArgs = func.__code__.co_varnames[:func.__code__.co_argcount]
	
	params = [ ":param %s: description" % methodArg for methodArg in methodArgs ]
	types = [ ":type %s: type description" % methodArg for methodArg in methodArgs ]
	returns = []
	if codeReturnsSomething(func):
		returns = [":return: return description",":rtype: the return type description"]

	txt = "\n".join(params + types + returns)

	return txt

def processFunction(func):
	funcName = func.func_name

	# Skip methods that start with '_' except for constructors
	if funcName.startswith('_') and not funcName == '__init__':
		return

	funcFilename = func.__code__.co_filename
	methodArgs = func.__code__.co_varnames[:func.__code__.co_argcount]
	
	params = [ ":param %s:" % methodArg for methodArg in methodArgs ]
	types = [ ":type %s:" % methodArg for methodArg in methodArgs ]
	returns = []
	if codeReturnsSomething(func):
		returns = [":return:",":rtype:"]

	expected = params + types + returns

	if inspect.getdoc(func) is None:
		raise DocstringTestError("Expected docstring",funcFilename,funcName)

	docstring = inspect.getdoc(func).split('\n')
	docstring = [ line.strip() for line in docstring ]
	docstring = [ line for line in docstring if line ]

	docstringWithParams = [ line for line in docstring if line.startswith(':param') or line.startswith(':type') or line.startswith(':return: ') or line.startswith(':rtype: ') ]

	for i in range(max(len(expected),len(docstringWithParams))):
		if i >= len(docstringWithParams):
			raise DocstringTestError("Expected '%s' in docstring" % expected[i],funcFilename,funcName)
		elif i >= len(expected):
			raise DocstringTestError("Unexpected '%s' in docstring" % docstringWithParams[i],funcFilename,funcName)
		elif not docstringWithParams[i].startswith(expected[i]):
			raise DocstringTestError("Expected '%s' in docstring" % expected[i],funcFilename,funcName)

	# If we have exactly the parameter info and nothing else, then we're missing a description (of some length) about what the function does
	if len(expected) == len(docstring):
		raise DocstringTestError("Expected description of function in docstring" ,funcFilename,funcName)


def processClass(c):
	for name,obj in inspect.getmembers(c):
		#print name,obj
		if inspect.ismethod(obj):
			processFunction(obj)

def processModule(m):
	for name,obj in inspect.getmembers(m):
		if inspect.isclass(obj):
			processClass(obj)
		elif inspect.isfunction(obj):
			processFunction(obj)
