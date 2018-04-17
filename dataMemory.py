class Memory:

	def __init__(self):
		self.setDefault()

	def setDefault(self):
		self.memory = [0, 0, 0, 0, 0, 0, 0]

	def get(self, address):
		return self.memory[address]

	def write(self, address, data):
		self.memory[address] = data