import registers
import mux
import alu
import instructionMemory

reg = registers.Registers()
IM = instructionMemory.Memory()
alu = alu.ALU()
PC = 0
#decode.Decode("addi $1, $2, $3")


def Fetch(PC):
	instruction = IM.getInstruction(reg.PC)
	reg.incrementPC()

	return (instruction)


def Decode(instruction, reg):		#instruction is a MIPS instruction
	insType = ""
	decodedIns = str(instruction).translate({ord(c): None for c in ','}).split() 		#translate removes the ',' from the string

	
	#decodedIns[0] is opcode
	
	for i in range(len(decodedIns))[1:]:
		decodedIns[i] = (str(decodedIns[i]).translate({ord(c): None for c in '$'})) #strip $ and put the remaining value in rd


	return decodedIns



def Execute(decodedIns, reg):
	if (decodedIns[0] in ("add", "sw", "add", "addi")):	#decodedIns[0] == opcode
		reg.writeAddr = decodedIns[1]
		reg.readAddr1 = decodedIns[2]
		reg.readAddr2 = decodedIns[3]

		alu.add(reg, decodedIns)

	if (decodedIns[0] in "addi"):
		reg.writeAddr = decodedIns[1]
		reg.readAddr1 = decodedIns[2]

		alu.add(reg, decodedIns)

	if (decodedIns[0] in "sub"):
		reg.writeAddr = decodedIns[1]
		reg.readAddr1 = decodedIns[2]
		reg.readAddr2 = decodedIns[3]

		alu.subtract(reg, decodedIns)

		print (reg.R4)
	if (decodedIns[0] in "subi"):
		reg.writeAddr = decodedIns[1]
		reg.readAddr1 = decodedIns[2]
		alu.subtract(reg, decodedIns)

		print (reg.R4)

	if (decodedIns[0] in "lw"):

		return 0
	if (decodedIns[0] in "sw"):
		return 0
	if (decodedIns[0] in "beq"):
		return 0
	if (decodedIns[0] in "or"):
		reg.writeAddr = decodedIns[1]
		reg.readAddr1 = decodedIns[2]
		reg.readAddr2 = decodedIns[3]

		alu.OR(reg, decodedIns)
		print (reg.R4)

	if (decodedIns[0] in "and"):
		reg.writeAddr = decodedIns[1]
		reg.readAddr1 = decodedIns[2]
		reg.readAddr2 = decodedIns[3]

		alu.AND(reg, decodedIns)
		print (reg.R4)

		return 0

def CPUState():
	print ("R0: ", reg.R0)
	print ("R1: ", reg.R1)
	print ("R2: ", reg.R2)
	print ("R3: ", reg.R3)
	print ("R4: ", reg.R4)

for x in IM.memory: #iterate through IM
	#Fetch()
	currentInstruction = Fetch(PC)
	decodedIns = Decode(currentInstruction, reg)

	print (decodedIns)
	Execute(decodedIns, reg)

	#Current registers
	CPUState()
				
	



#Fetch()


#TODO
#Decode needds to update registers
#Execute
#Jump instructions?
#

