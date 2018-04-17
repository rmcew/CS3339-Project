import registers
import mux
import alu
import instructionMemory
import dataMemory


reg = registers.Registers()
IM = instructionMemory.Memory()
DM = dataMemory.Memory()
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
	if (decodedIns[0] in ("add")):	#decodedIns[0] == opcode
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
		reg.writeAddr = decodedIns[1]
		temp = str(decodedIns[2]).split('(')
		offset = temp[0]
		decodedIns[2] = str(temp[1]).translate({ord(c): None for c in ('$', ')')})
		reg.readAddr1 = decodedIns[2]

		alu.load(reg, decodedIns, offset, DM)

	if (decodedIns[0] in "sw"):
		reg.readAddr1 = decodedIns[1]
		temp = str(decodedIns[2]).split('(')
		offset = temp[0]
		decodedIns[2] = str(temp[1]).translate({ord(c): None for c in ('$', ')')})

		alu.store(reg, decodedIns, offset, DM)


	if (decodedIns[0] in "j"):
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

