class Memory:

	def __init__(self):
		self.setDefault()

	def setDefault(self):
		self.memory = ['00000010001100101000000000100000','b','c','d','e','f','g','h']

	def getInstruction(self, address):
		return self.memory[address]
