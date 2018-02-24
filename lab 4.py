# class Finalmark(object):
# 	"""docstring for ClassName"""
# 	def __init__(self, matricNo): # initialization
# 		self.matric = matricNo    #attribute initialise
# 		self.calculusMark = None
# 		self.dynamicMark = None

# 	def calculus(self, mark):
# 		self.calculusMark = mark

# 	def dynamic(self, mark):
# 		self.dynamicMark = mark

# 	def printResult(self):
# 		print("Matric No : ",self.matric)	
# 		print(" ")
# 		print("Calculus : ",self.calculusMark)
# 		print("Dynamic : ",self.dynamicMark)


# Malik = Finalmark(1510022)
# Malik.calculus(99)
# Malik.dynamic(49)
# Malik.printResult()


#class definition
class Node(object):
	"""docstring for Node"""
	def __init__(self, data):
		
		self.data = data
		self.next_node = next_node


#function/method defination

	def getData(self):
		return self.data

	def getNext(self):
		return self.next_node

	def setData(self, newdata):
		self.data - newdata

	def setNext(self, newnext):
		self.next_node = newnext


#new class

class MyLList(object):
	"""docstring for MyLList"""
	def __init__(self):
		self.head = None

	def isEmpty(self):
		return self.head == None

	def add(self, item):
		new_node = Node(item)
		new_node.setNext(self.head)
		self.head = new_node

	def size(self):
		current = self.head
		count = 0
		while current != None:
			count += 1
			current = current.getNext()
		return count

	def search(self, item):
		current = self.head
		found = False
		while current != None and not found:
			if current.getData() == item:
				found = True
			else:
				current = current.getNext()

		return found

	def remove(self, item):
		current = self.head
		previous = None
		found = False
		while not found:
			



			if current.getData() == item:
				found = True
			else:
				previous = current
				current = current.getNext()

		if previous == None:
			self.head = current.getNext()
		else:
			previous.setNext(current.getNext())
		


	def printList(self):
		current = self.head
		while current != None:
			print(current.data)
			current = current.next_node

#this is the basic program define

while True:
	print("+++++++++++++++++++++++++++++++++")
	print("1. create the list")
	print("2. insert in the beginning")
	print("3.remove from the list")
	print("4.count element in the list")
	print("5.display")
	print("6.exit")
	print("+++++++++++++++++++++++++++++++++")

	choice=int(input("enter your choice:"))

	if choice==1:
		mylist=mylist()
		print("the list has been created")
	elif choice==2:
		item=int(input("enter the number to be added:"))
		mylist.add(item)
	elif choice==3:
		item=int(input("enter the number to be remove:2"))
		mylist.remove(item)
    elif choice==4:
        print("the number of elemnt in the list:",mylist.size())
    elif choice==5:
    	print("the elements in the list:")
    	mylist.printlist()
    else:
    	 break
