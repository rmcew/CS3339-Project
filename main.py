import registers
import mux
import alu
import instructionMemory
import dataMemory


reg = registers.Registers()
IM = instructionMemory.Memory()
DM = dataMemory.Memory()
alu = alu.ALU()
currentInstruction = 0
#decode.Decode("addi $1, $2, $3")

with open('test') as f:
	IM.memory = [line.rstrip('\n') for line in open('test')]
	print (IM.memory)

def Fetch(PC):
	#currentInstruction = IM.getInstruction(reg.PC)

	Decode(IM.getInstruction(reg.PC), reg)

	reg.incrementPC()



def Decode(instruction, reg):		#instruction is a MIPS instruction
	insType = ""
	decodedIns = str(instruction).translate({ord(c): None for c in ','}).split() 		#translate removes the ',' from the string

	
	#decodedIns[0] is opcode
	
	for i in range(len(decodedIns))[1:]:
		decodedIns[i] = (str(decodedIns[i]).translate({ord(c): None for c in '$'})) #strip $ and put the remaining value in rd

	print ("DECODEDINS: ", decodedIns)
	Execute(decodedIns, reg) 



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
		reg.PC = int(decodedIns[1]) - 1
		#return 0

	if (decodedIns[0] in "beq"):
		reg.readAddr1 = decodedIns[1]
		reg.readAddr2 = decodedIns[2]
		
		alu.branch(reg, decodedIns)

						
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

while True: 

	try: 
		Fetch(reg.PC) #iterate through IM

	except:
		print ("reached the end")
		break
	#print ("CURRENT INSTRUCTION", currentInstruction)
	#decodedIns = Decode(currentInstruction, reg)

	#print (decodedIns)
	#Execute(decodedIns, reg)
	print ("Current PC Value: ", reg.PC)

	#Current registers
	CPUState()
				
	



#Fetch()


#TODO
#Decode needds to update registers
#Execute
#Jump instructions?
#

