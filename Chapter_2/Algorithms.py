import time

def sumOfN(n):

	theSum = 0
	for i in range(1, n+1):
		theSum = theSum + 1

	return theSum


def sumOfN2(n):

	start = time.time()	

	theSum = 0
	for i in range(1, n+1):
		theSum = theSum + 1

	end = time.time()	

	return theSum, end-start


if __name__ == "__main__":

	number = 100000
	answer = sumOfN(number)
	print("\nTesting sumOfN for n = %d\nAnswer: %d\n" % \
			(number, answer))

	answer2, timer2 = sumOfN2(number)
	
	print("Testing sumOfN2 for n = %d\nAnswer: %d\nTime: %f\n" % \
			 (number, answer2, timer2))
