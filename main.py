import registers
import mux
import alu
import memory
import gates

#def fetch()
regObj = registers.Registers()

while regObj.pc <=int(50):
	regObj.incrementPC()
	print regObj.pc
test