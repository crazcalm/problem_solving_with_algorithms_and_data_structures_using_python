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

def anagramSolution1(s1, s2): # Checking off
	
	alist = list(s2)

	pos1 = 0
	stillOK = True

	while pos1 < len(s1) and stillOK:
		
		pos2 = 0
		found = False

		while pos2 < len(alist) and not found:
			if s1[pos1] == alist[pos2]:
				found = True
				
			else:
				pos2 = pos2 + 1

		if found:
			alist[pos2] = None
		
		else:
			stillOK = False

		pos1 += 1

	return stillOK

def anagramSolution2(s1,s2): # Sort and compare

	alist1 = list(s1)
	alist2 = list(s2)

	alist1.sort()
	alist2.sort()

	pos = 0
	matches = True

	while pos < len(s1) and matches:
		if alist1[pos] == alist2[pos]:
			pos += 1

		else:
			matches = False

	return matches

def anagramSolution4(s1, s2): # Count and Compare
	c1 = [0] * 26
	c2 = [0] * 26

	for i in range(len(s1)):
		pos = ord(s1[i]) - ord("a")
		c1[pos] = c1[pos] + 1

	for i in range(len(s2)):
		pos = ord(s2[i]) - ord('a')
		c2[pos] = c2[pos] + 1

	j = 0
	stillOK = True
	while j<26 and stillOK:
		if c1[j] == c2[j]:
			j = j + 1
		else:
			stillOK = False

	return stillOK


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

		print("\nsumOfN2(%d) --> Answer: %d, Time: %f" % \
				(n, sum2, time2))
	
		print("sumOfN3(%d) --> Answer: %d, Time: %f" % \
				(n, sum3, time3))
	

	print("\nTesting anagram Solutions:\n")
	word1 = "marcus"
	word2 = "sucram"
	word3 = "loser"

	print("anagramSolution1: %s vs %s \nAnswer: %s\n" % \
			(word1, word2, anagramSolution1(word1,word2)))

	print("anagramSolution1: %s vs %s \nAnswer: %s\n" % \
			(word1, word3, anagramSolution1(word1,word3)))

	print("anagramSolution2: %s vs %s \nAnswer: %s\n" % \
			(word1, word2, anagramSolution2(word1,word2)))

	print("anagramSolution2: %s vs %s \nAnswer: %s\n" % \
			(word1, word3, anagramSolution2(word1,word3)))

	print("anagramSolution4: %s vs %s \nAnswer: %s\n" % \
			(word1, word2, anagramSolution4(word1,word2)))

	print("anagramSolution4: %s vs %s \nAnswer: %s\n" % \
			(word1, word3, anagramSolution4(word1,word3)))

	
