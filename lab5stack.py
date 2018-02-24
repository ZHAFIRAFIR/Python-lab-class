class Stack(object):
	"""docstring for ClassName"""
	def __init__(self):
		self.myStack= []
		
	def push(self,item):
		self.myStack.append(item)

	def pops(self):
		self.myStack.pop()

	def top(self):
		return self.myStack[-1]

	def size(self):
		return len(self.myStack)

	def isEmpty(self):
		return self.myStack==[]
#end of the class declaration


def printStack(myStack):
	for element in reversed(myStack):
		print(element)

stackobj=Stack()
stackobj.push(99)
stackobj.push(8)
stackobj.push(59)
printStack(stackobj.myStack)


print("the top of the stack is",stackobj.top())
print("the size of the stack is",stackobj.size())

stackobj.pops()
printStack(stackobj.myStack)

print("is the stack is empty?",stackobj.isEmpty())