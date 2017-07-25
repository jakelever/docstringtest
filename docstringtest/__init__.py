
import inspect

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
	methodArgs = func.__code__.co_varnames[:func.__code__.co_argcount]


def processClass(c):
	for name,obj in inspect.getmembers(c):
		#print name,obj
		if inspect.ismethod(obj):
			print(name)
			processFunction(obj)

def processModule(m):
	for name,obj in inspect.getmembers(m):
		if inspect.isclass(obj):
			print("#",name)
			processClass(obj)
