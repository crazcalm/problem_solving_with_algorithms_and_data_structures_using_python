class Stack:

	def __init__(self):

		self.items = []

	def __str__(self):
		
		result = ""
		for index, item in enumerate(self.items):
			result += "\n%s: %s" % (index, item)
		return result

	def __repr__(self):
		return self.__str__()

	def isEmpty(self):
		return self.items == []

	def push(self, item):
		return self.items.append(item)
	
	def pop(self):
		return self.items.pop()

	def peek(self):
		return self.items[len(self.items) - 1]

	def size(self):
		return len(self.items)


if __name__ == "__main__":
	
	print("Testing the Stack class:\n")

	test = Stack()
	print("isEmpty: %s\n" % test.isEmpty())
	test.push("All I say are lies!")
	test.push("Marcus is the Man!!!")
	print("push: %s\n" % test)
	print("pop: %s\n" % test.pop())
	print("peek: %s\n" % test.peek())
	print("size: %s\n" % test.size())
