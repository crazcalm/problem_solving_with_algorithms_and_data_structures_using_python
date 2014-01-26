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

	def setNextPin(self, source):
		if self.pinA == None:
			self.pinA = source

		else:
			if self.pinB == None:
				self.pinB = source
			
			else:
				raise RuntimeError("Error: NO EMPTY PINS")


class UnaryGate(LogicGate):
	
	def __init__(self, n):
		super().__init__(n)

		self.pinA = None

	#def getPin(self):

	#	return int(input("Enter Pin iput for gate " + \
	#						self.getLabel()+"-->"))

	def setNextPin(self, source):
		if self.pinA == None:
			self.pinA = source

		else:
			if self.pinB == None:
				self.pinB = source
			
			else:
				raise RuntimeError("Error: NO EMPTY PINS")

	def getPinA(self):
		if self.pinA == None:
			return int(input("Enter Pin A input for gate " + \
						self.getLabel() +"-->"))

		else:
			return self.pinA.getFrom().getOutput()

class AndGate(BinaryGate):

	def __init__(self, n):
		super().__init__(n)

	def performGateLogic(self):
		
		a = self.getPinA()
		b = self.getPinB()

		if a==1 and b==1:
			return 1
		else:
			return 0

class OrGate(BinaryGate):

	def __init__(self, n):
		super().__init__(n)

	def performGateLogic(self):

		a = self.getPinA()
		b = self.getPinB()

		if a==1 or b==1:
			return 1
			
		else:
			return 0

class NotGate(UnaryGate):

	def __init__(self, n):
		super().__init__(n)

	def performGateLogic(self):
		
		a = self.getPinA()

		if a ==1:
			return 0
		
		else:
			return 1

class Connector:
		
	def __init__(self, fgate,tgate):
		self.fromgate = fgate
		self.togate = tgate

		tgate.setNextPin(self)

	def getFrom(self):
		return self.fromgate

	def getTo(self):
		return self.togate	


if __name__ == "__main__":
	
	print("Testing the AndGate:")
	g1 = AndGate("G1")
	g1.getOutput()
	print("Answer: %s\n" % (g1.output))

	print("Testing the OrGate:")
	g2 = OrGate("G2")
	g2.getOutput()
	print("Answer: %s\n" % (g2.output))

	print("Testing the NotGate:")
	g3 = NotGate("G3")
	g3.getOutput()
	print("Answer: %s\n" % (g3.output))

	print("Testing Connector(s):\n")
	g1 = AndGate("G1")
	g2 = AndGate("G2")
	g3 = OrGate("G3")
	g4 = NotGate("G4")
	c1 = Connector(g1,g3)
	c2 = Connector(g2,g3)
	c3 = Connector(g3,g4)

	g4.getOutput()
	print("\nAnd, And, Or, Not Gates")
	print("Answer: %s" % (g4.output))
