class Memory:

	def __init__(self):
		self.setDefault()

	def setDefault(self):
		#self.memory = ['sw $2, 8($2)']   #'lw $1, 4($2)', 'lw $3, 16($2)', 'sw $4, 8($2)', 'j label', 'addi $4, $1, 3'
		self.labelList = [[], []]

	def getInstruction(self, address):
		return self.memory[address]
