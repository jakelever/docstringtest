
import inspect

def processMethod(m):
	methodArgs = m.__code__.co_varnames[:m.__code__.co_argcount]
	

def processClass(c):
	for name,obj in inspect.getmembers(c):
		#print name,obj
		if inspect.ismethod(obj):
			print name
			processMethod(obj)

def processModule(m):
	for name,obj in inspect.getmembers(m):
		if inspect.isclass(obj):
			print "#",name
			processClass(obj)
