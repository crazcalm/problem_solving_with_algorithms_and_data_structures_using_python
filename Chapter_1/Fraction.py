class Fraction:
	"""
	A module to deal with basic fractions.
	"""
	
	def __init__(self, top, bottom):

		common = gcd(top, bottom)
		
		self.num = top //common
		self.den = bottom //common


	def __str__(self):
		
		return str(self.num) +  "/" + str(self.den)

	def __repr__(self):

		return self.__str__()

	def show(self):
		
		print (self.num, "/", self.den)

	def __add__(self, otherfraction):

		newnum = self.num * otherfraction.den + \
				self.den * otherfraction.num

		newden = self.den * otherfraction.den

		return Fraction(newnum, newden)
	
	def __eq__(self, other):
		
		firstnum = self.num * other.den
		secondnum = other.num * self.den

		return firstnum == secondnum

	def __sub__(self, other):

		newnum = self.num * other.den - \
			     self.den * other.num

		newden = self.den * other.den

		return Fraction(newnum, newden)

	def getNum(self):
		
		return self.num

	def getDen(self):
	
		return self.den


def squareroot(n):
	"""
	Newton's Method for square roots
	"""

	root = n/2	#initial guess will be 1/2 of n
	for k in range(20):
		root = (1/2)*(root + (n/root))

	return root

def gcd(m,n):
	"""
	Greatest common denominator
	"""

	while m%n !=0:
		oldm = m
		oldn = n

		m = oldn
		n = oldm %oldn

	return n
	
		
if __name__ == "__main__":
	test = Fraction(1,2)
	test2 = Fraction(6,8)
	test3 = Fraction(4,8)

	print("Testing BASIC Functionality: \n")
	print("Fraction A = %s" % (test))
	print("Fraction B = %s \n" % (test2))
	print("%s + %s = %s\n" % (test, test2, test+test2))
	print("The gcd(100,40) = %d" %  gcd(100,40))
	print("The sqrt(10) = %f " % squareroot(10))
	print("Testing equality: %s == %s --> %s" % (test, test, test==test))
	print("Testing equality: %s == %s --> %s" % (test, test2, test==test2))
	print("Testing equality: %s == %s --> %s\n" % (test, test3, test==test3))
	
	print("Testing getNum for Fraction A: %s" % (test.getNum()))
	print("Testing getDen for Fraction A: %s\n" % (test.getDen()))

	print("Testing Subtraction: %s - %s = %s" % (test, test2, test - test2))
	print("Testing Subtraction: %s - %s = %s" % (test2, test, test2 - test))
	print("Testing Subtraction: %s - %s = %s\n" % (test, test, test - test))


