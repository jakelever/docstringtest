
import inspect

def codeReturnsSomething(m):
	sourceCode = inspect.getsource(m).split('\n')
	for line in sourceCode:
		tokens = line.strip().split()
		if len(tokens) >= 2 and tokens[0] == 'return':
			return True
	return False

def generateDocstring(m):
	methodArgs = m.__code__.co_varnames[:m.__code__.co_argcount]
	
	params = [ ":param %s: description" % methodArg for methodArg in methodArgs ]
	types = [ ":type %s: type description" % methodArg for methodArg in methodArgs ]
	returns = []
	if codeReturnsSomething(m):
		returns = [":return: return description",":rtype: the return type description"]

	txt = "\n".join(params + types + returns)

	return txt

def processMethod(m):
	methodArgs = m.__code__.co_varnames[:m.__code__.co_argcount]
	

def processClass(c):
	for name,obj in inspect.getmembers(c):
		#print name,obj
		if inspect.ismethod(obj):
			print(name)
			processMethod(obj)

def processModule(m):
	for name,obj in inspect.getmembers(m):
		if inspect.isclass(obj):
			print("#",name)
			processClass(obj)
