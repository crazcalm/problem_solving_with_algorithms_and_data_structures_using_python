def sumOfN(n):
	theSum = 0
	for i in range(1, n+1):
		theSum = theSum + 1

	return theSum


if __name__ == "__main__":
	print("Testing sumOFN for n = %s Answer: %s" % (10, sumOfN(10)))
