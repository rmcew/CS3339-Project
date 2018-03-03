class ALU:
	def __init__(self):
		self.setDefault()

	def setDefault(self):

		return 0

	def Decode(self, instruction, reg):
		opcode = instruction[:6]
		rs = instruction[6:11]
		rt = instruction[11:16]
		rd = instruction[16:21]
		shamt = instruction[21:26]
		funct = instruction[26:32]
		return opcode, rs, rt, rd, shamt, funct
		



def readData1():
	print "test"
def readData2(mux):
	print "test"
