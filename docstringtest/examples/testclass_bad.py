
class ExampleBadClass:
	def __init__(self, varA, varB, varC):
		pass

	def _shouldBeIgnored(self, varA, varB):
		pass

	def staticMethod(varA):
		"""
		Some basic description

		:param varA: description
		"""
		pass
	
	def staticMethodWithReturn(varA):
		"""
		Some basic description

		:param varA: description
		:type varA: type description
		"""
		return 1

	def basicMethod(self,varA,varB):
		"""
		Some basic description
		"""
		pass

	def basicMethodWithReturn(self,varA,varB):
		"""
		Some basic description

		:param self: description
		:param varA: description
		:type self: type description
		:type varA: type description
		:return: return description
		:rtype: the return type description
		"""
		return 1

	def basicMethodWithYield(self,varA,varB):
		"""
		Some basic description

		:param self: description
		:param varA: description
		:param varB: description
		:type self: type description
		:type varA: type description
		:type varB: type description
		"""
		for i in range(10):
			yield i

	def staticMethodNoVariables():
		"""
		Some basic description
		
		:return: return description
		:rtype: the return type description
		"""
		pass

	def staticMethodNoVariablesWithReturn():
		"""
		:return: return description
		:rtype: the return type description
		"""
		return 1

	def staticMethodNoVariablesWithYield():
		for i in range(10):
			yield i
