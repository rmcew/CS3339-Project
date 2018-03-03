import registers
import mux
import alu
import memory
import gates

reg = registers.Registers()
mem = memory.Memory()
alu = alu.ALU()

#*******************************************************
#	Get next instruction from memory using PC as index *
#	Increment PC									   *
#*******************************************************
def Fetch():
	print reg.programCounter
	reg.instructionRegister = mem.getInstruction(reg.programCounter)
	reg.incrementPC()
Fetch()

def Decode(instruction, reg):
	print alu.Decode(instruction, reg)

Decode(reg.instructionRegister, reg)