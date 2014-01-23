class Fraction:
	"""
	A module to deal with basic fractions.
	"""
	
	def __init__(self, top, bottom):
		
		self.num = top
		self.den = bottom

	def __str__(self):
		
		return str(self.num) +  "/" + str(self.den)

	def show(self):
		
		print (self.num, "/", self.den)

	def __add__(self, otherfraction):

		newnum = self.num * otherfraction.den + \
				self.den * otherfraction.num

		newdem = self.den * otherfraction.den

		common = gcd(newnum, newden)
		
		return Fraction(newnum//common, newden//common)


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
	
		
