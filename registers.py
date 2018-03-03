class Registers:

	def __init__(self):
		self.setDefault()

	def setDefault(self):
		self.programCounter = 0
		self.instructionRegister = 0
		self.v0 = 0
		self.v1 = 0
		self.v2 = 0
		self.v3 = 0
		self.v4 = 0

	def incrementPC(self):
		self.programCounter +=1



def readRegister1(instruction):
	print "test"
def readRegister2(instruction):
	print "test"

def writeRegister(instruction):
	print "test"

def writeData(mux):
	print "test"

def readData1():
	print "test"

def readData2():
	print "test"

def updatePC():
	pc=pc+bin(4)



