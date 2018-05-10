import registers
import alu
import instructionMemory
import dataMemory


reg = registers.Registers()
IM = instructionMemory.Memory()
DM = dataMemory.Memory()
alu = alu.ALU()


with open('test') as f:
	IM.memory = [line.rstrip('\n') for line in open('test')]
	print (IM.memory)

def Fetch(PC):
	Decode(IM.getInstruction(reg.PC), reg)
	reg.incrementPC()



def Decode(instruction, reg):		#instruction is a MIPS instruction
	decodedIns = str(instruction).translate({ord(c): None for c in ','}).split() 		#translate removes the ',' from the string

	
	print ("CURRENT INSTRUCTION: ", instruction)
	
	for i in range(len(decodedIns))[1:]:
		decodedIns[i] = (str(decodedIns[i]).translate({ord(c): None for c in '$'})) #strip $ and put the remaining value in rd

	#Instructions that use read register 1, read register 2, and write register
	if (decodedIns[0] in ("add", "sub", "mult", "or", "and")):
		reg.writeAddr = decodedIns[1]
		reg.readAddr1 = decodedIns[2]
		reg.readAddr2 = decodedIns[3]


	#Instructions that use write register and read register 1
	if (decodedIns[0] in ("addi", "sll", "srl")):
		reg.writeAddr = decodedIns[1]
		reg.readAddr1 = decodedIns[2]

	if (decodedIns[0] in ("beq")):
		reg.readAddr1 = decodedIns[1]
		reg.readAddr2 = decodedIns[2]

	Execute(decodedIns, reg) 



def Execute(decodedIns, reg):
	if (decodedIns[0] in ("add", "addi")):	#decodedIns[0] == opcode
		alu.add(reg, decodedIns)

	if (decodedIns[0] in ("sub")):
		alu.subtract(reg, decodedIns)

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

	if (decodedIns[0] in "mult"):
		alu.mult(reg, decodedIns)

	if (decodedIns[0] in "sll"):
		alu.sll(reg, decodedIns)


	if (decodedIns[0] in "srl"):
		alu.srl(reg, decodedIns)

	if (decodedIns[0] in "j"):
		reg.PC = int(decodedIns[1]) - 1

	if (decodedIns[0] in "beq"):	
		alu.branch(reg, decodedIns)

						
	if (decodedIns[0] in "or"):
		alu.OR(reg, decodedIns)

	if (decodedIns[0] in "and"):
		alu.AND(reg, decodedIns)

def Status():

	print ("PC: ", reg.PC)
	print ("R0: ", reg.R0)
	print ("R1: ", reg.R1)
	print ("R2: ", reg.R2)
	print ("R3: ", reg.R3)
	print ("R4: ", reg.R4)

	print ("Data MEM: ", DM.memory)

	print ("\n")

while True: 

	try: 
		Fetch(reg.PC) #iterate through IM

	except:
		print ("END")
		break

	Status()