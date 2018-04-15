class Memory:

	def __init__(self):
		self.setDefault()

	def setDefault(self):
		self.memory = [1, 2, 3, 4, 5, 6, 7]

	def get(self, address):
		return self.memory[address]

	def write(self, address, data):
		self.memory[address] = data