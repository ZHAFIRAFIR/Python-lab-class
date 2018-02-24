#class definition
class Node(object):
	"""docstring for Node"""
	def __init__(self, data):
		
		self.data = data #node
		self.next_node = None #pointer
		self.prev = None


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

class Queue(object):
	"""docstring for MyLList"""
	def __init__(self):

		self.head = None
		self.tail = None

	def enqueue(self, item):
		new_node = Node(item)
		# new_node.setNext()
		if self.head == None and self.tail == None:
			self.tail = new_node 
			self.head = self.tail
		else:
			new_node.setNext(self.head) #append new node
			self.head = new_node

	def dequeue(self):
		if self.tail == None:
			print("Stack is empty")
			return None

		else:
			current = self.head
			prev = current
			while current.getNext() != None: #the last element will have next == None
				prev = current
				current = current.getNext()
			
		# At this point, current will be pointing to the last element in the list
		self.tail = prev
		prev.setNext(None)
		print("Dequeued ")


	def printList(self):
		current = self.head
		while current != None:
			print(current.data)
			current = current.next_node

	def size(self):
		current = self.head
		count = 0
		while current != None:
			count += 1
			current = current.getNext()
		return count


	def isEmpty(self):
		return self.head == None






#main Program
queue1 = Queue()
while True:
	print("#######################################")
	print(" ")
	print("1. Enqueue")
	print("2. Dequeue")
	print("3. Size ")
	print("4. Display")
	print("5. isEmpty")
	print("6. Exit")
	print("#######################################")

	choice = int(input("Please select choice :"))

	if choice == 1:
		status = True
		while (status == True):
			item = int(input("Enter the number to be enqueue : "))
			queue1.enqueue(item)
			status = str(input("Do you wish to enter more number?(Y/N) : "))
			if (status == 'y' or status == 'Y'):
				status = True
			elif (status == 'N' or status == 'n'):
				status = False

	elif choice == 2:
		
		queue1.dequeue()

	elif choice == 3:
		print("The size of the Queue is ", queue1.size())


	elif choice == 4:
		print("THE QUEUE :")
		queue1.printList()

	elif choice == 5:
		condition = queue1.isEmpty()	

		if condition == False:
			print("The List is Not Empty")
		else:
			print("The List is Empty")

	elif choice == 6:
		break

	else:
		print("wrong choice!!")
