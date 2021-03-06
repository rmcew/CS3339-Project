class ALU:
	def __init__(self):
		self.setDefault()

	def setDefault(self):

		return 0

	#ALU add used for lw, sw, add, addi
	def add(self, reg, decodedIns):
		if("addi" in decodedIns):
			reg.writeData(int(reg.readData1()) + int(decodedIns[3]))
		else:
			reg.writeData(int(reg.readData1()) + int(reg.readData2()))

	#ALU subtract used for beq, sub
	def subtract(self, reg, decodedIns):
		if ("subi" in decodedIns):
			reg.writeData(int(reg.readData1()) - int(decodedIns[3]))
		else:
			print (reg.readData1(), reg.readData2())
			reg.writeData(int(reg.readData1()) - int(reg.readData2()))

	def branch(self, reg, decodedIns):
		if ("beq" in decodedIns):
			if (int(reg.readData1()) == int(reg.readData2())):
				reg.PC = reg.PC - (abs(int((int(decodedIns[3])/4))) + 1)

		if ("beqz" in decodedIns):
			return 0

	def mult(self, reg, decodedIns):
		reg.writeData(int(reg.readData1() * int(reg.readData2())))

	#ALU OR used for or
	def OR(self, reg, decodedIns):
		reg.writeData(int(reg.readData1()) | int(reg.readData2()))
		return 0

	#ALU AND used for and
	def AND(self, reg, decodedIns):
		reg.writeData(int(reg.readData1()) & int(reg.readData2()))
		return 0

	def load(self, reg, decodedIns, offset, DM):
		dmAddress = (int(int(offset)/4) + int(reg.readData1()) - 1)
		reg.writeData(((DM.get(dmAddress))))

	def store(self, reg, decodedIns, offset, DM):
		dmAddress = int(int(offset)/4) + int(decodedIns[2])
		DM.write(dmAddress, reg.readData1())

	def sll(self, reg, decodedIns):
		reg.writeData(int(reg.readData1()) * (int(2**int(decodedIns[3]))))

	def srl(self, reg, decodedIns):
		print (int(reg.readData1())/ int(int(2**int(decodedIns[3]))))
		reg.writeData(int(reg.readData1())/ int(int(2**int(decodedIns[3]))))		
		



		



	def readData1():
		print ("test")
	def readData2(mux):
		print ("test")
