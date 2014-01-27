import time

def sumOfN(n):

	theSum = 0
	for i in range(1, n+1):
		theSum = theSum + i

	return theSum


def sumOfN2(n):

	start = time.time()	

	theSum = 0
	for i in range(1, n+1):
		theSum = theSum + i

	end = time.time()	

	return theSum, end - start

def sumOfN3(n):

	start = time.time()

	theSum = (n*(n+1))/2
	
	end = time.time()
	
	return theSum, end - start

if __name__ == "__main__":

	number = 100000
	answer = sumOfN(number)
	print("\nTesting sumOfN for n = %d\nAnswer: %d\n" % \
			(number, answer))

	answer2, timer2 = sumOfN2(number)
	
	print("Testing sumOfN2 for n = %d\nAnswer: %d\nTime: %f\n" % \
			 (number, answer2, timer2))

	answer3, timer3 = sumOfN3(number)
	print("Testing sumOfN3 for n = %d\nAnswer: %d\nTime: %f\n" % \
			 (number, answer3, timer3))

	print("Benchmark measurements for sumOfN2 and sumOfN3:")
	test_set = (10000, 100000, 1000000, 10000000, 100000000)

	for n in test_set:
		sum2, time2 = sumOfN2(n)
		sum3, time3 = sumOfN3(n)

		print("\nsumOfN2 --> Answer: %d, Time: %f" % \
				(sum2, time2))
	
		print("sumOfN3 --> Answer: %d, Time: %f" % \
				(sum3, time3))
	
