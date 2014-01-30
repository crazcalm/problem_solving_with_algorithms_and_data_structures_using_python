class Stack:

	def __init__(self):

		self.items = []

	def __str__(self):
		return ", ".join(self.items)

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
	print("isEmpty: %s" % test.isEmpty())
	test.push("All I say are lies!")
	test.push("Marcus is the Man!!!")
	print("push: %s" % test)
	print("pop: %s" % test.pop())
	print("peek: %s" % test.peek())
	print("size: %s" % test.size())
