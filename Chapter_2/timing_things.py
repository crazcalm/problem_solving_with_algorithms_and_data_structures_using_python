from timeit import Timer

def test1(): # slowest
	l = []
	for i in range(1000):
		l = l + [i]

def test2(): # 3rd place
	l = []
	for i in range(1000):
		l.append(i)

def test3(): # 2cd place
	l = [i for i in range(1000)]

def test4(): #fastest
	l = list(range(100))

if __name__ == "__main__":
	
	t1 = Timer("test1()", "from __main__ import test1")
	print("concat ", t1.timeit(number=1000), "milliseconds")
	t2 = Timer("test2()", "from __main__ import test2")
	print("append ", t2.timeit(number=1000), "milliseconds")
	t3 = Timer("test3()", "from __main__ import test3")
	print("comprehension ", t3.timeit(number=1000), "milliseconds")
	t4 = Timer("test4()", "from __main__ import test4")
	print("list range ", t4.timeit(number=1000), "milliseconds")

