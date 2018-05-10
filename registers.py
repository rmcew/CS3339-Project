class Registers:

	def __init__(self):
		self.setDefault()

	def setDefault(self):
		self.PC = 0
		self.instructionRegister = 0
		self.R0 = 0
		self.R1 = 0
		self.R2 = 0
		self.R3 = 0
		self.R4 = 0
		
		self.readAddr1 = 0
		self.readAddr2 = 0
		self.writeAddr = 0


	def incrementPC(self):
		self.PC +=1


	def writeData(self, data):

		if (self.writeAddr == "0"):
			self.R0 = data
		if (self.writeAddr == "1"):
			self.R1 = data
		if (self.writeAddr == "2"):
			self.R2 = data
		if (self.writeAddr == "3"):
			self.R3 = data
		if (self.writeAddr == "4"):
			self.R4 = data


	def readData1(self):

		if (self.readAddr1 == "0"):
			return self.R0
		if (self.readAddr1 == "1"):
			return self.R1
		if (self.readAddr1 == "2"):
			return self.R2
		if (self.readAddr1 == "3"):
			return self.R3
		if (self.readAddr1 == "4"):
			return self.R4


	def readData2(self):
		if (self.readAddr2 == "0"):
			return self.R0
		if (self.readAddr2 == "1"):
			return self.R1
		if (self.readAddr2 == "2"):
			return self.R2
		if (self.readAddr2 == "3"):
			return self.R3
		if (self.readAddr2 == "4"):
			return self.R4			

