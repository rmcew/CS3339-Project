import instructionMemory
import registers


class Decode:
	def __init__(self):
		self.setDefault()
		#self.reg = registers.Registers()

	def setDefault(self):
		self.insType = ""
		return 0

	def Decode(self, instruction, reg):		#instruction is a MIPS instruction
		parsedInstruction = str(instruction).translate({ord(c): None for c in ','}).split() 		#translate removes the ',' from the string
		if (parsedInstruction[0] in ("add", "and", "sll", "slt", "jr", "sub", "srl", "or",)):
			self.insType = "R"
			print ("R-Type Instruction")

		if (parsedInstruction[0] in ("addi", "beq", "andi", "bne", "lw", "sw")):
			self.insType = "I"
			print ("I-Type Instruction")

		if (parsedInstruction[0]) in ("j"):
			self.insType = "J"
			print ("J-Type Instruction")

		#print (parsedInstruction[1])
		#print (parsedInstruction[2])
		#print (parsedInstruction[3])


		#R-Type instruction: opcode $rd, $rs, $rt
		if (self.insType == "R"):
			opcode = parsedInstruction[0]
			rd = str(parsedInstruction[1]).translate({ord(c): None for c in '$'}) #strip $ and put the remaining value in rd
			rs = str(parsedInstruction[2]).translate({ord(c): None for c in '$'}) #strip $ and put the remaining value in rs
			rt = str(parsedInstruction[3]).translate({ord(c): None for c in '$'}) #strip $ and put the remaining value in rt
			
			reg.updateRegAddr(rd, rs, rt)

			#reg.regWrite(rd)


			return (opcode, dest, source1, source2)

		#I-Type instruction: opcode $rt, $rs, imm
		if (self.insType == "I"):
			opcode = parsedInstruction[0]
			rt = parsedInstruction[1]
			imm = parsedInstruction[2]
			
			return (opcode, rt, imm)

		if (self.insType == "J"):
			opcode = parsedInstruction[0]
			target = parsedInstruction[1]

			return (opcode, target)

