"""
We are creating Logic Gates.

In laymen terms, we are creating binary and unary
operations (and, or, and not statements).

There are only two possible inputs (1, 0):

1 = True
0 = False
"""
class LogicGate:

	def __init__(self, n):

		self.label = n
		self.output = None

	def getLabel(self):
	
		return self.label

	def getOutput(self):

		self.output = self.performGateLogic()
		return self.output

class BinaryGate(LogicGate):

	def __init__(self, n):
		super().__init__(n)

		self.pinA = None
		self.pinB = None

	def getPinA(self):

		return int(input("Enter Pin A input for gate " + \
							self.getLabel()+"-->"))

	def getPinB(self):

		return int(input("Enter Pin B input for gate " + \
							self.getLabel()+"-->"))

class UnaryGate(LogicGate):
	
	def __init__(self, n):
		super().__init__(n)

		self.pin = None

	def getPin(self):

		return int(input("Enter Pin iput for gate " + \
							self.getLabel+"-->"))

class AndGate(BinaryGate):

	def __init__(self, n):
		super().__init__(n)

	def performGateLogic(self):
		
		a = self.getPinA()
		b = self.getPinB()

		# This is only half of an And 
		# cases?! Why?
		if a==1 and b==1:
			return 1
		else:
			return 0


if __name__ == "__main__":
	
	print("Testing the AndGate:\n")
	g1 = AndGate("G1")
	g1.getOutput()
	print("Answer: %s" % (g1.output))
