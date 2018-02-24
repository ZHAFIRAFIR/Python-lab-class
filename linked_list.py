#class definition
'''class Node(object):
	def __init__(self, data):
		self.data = data#node
		self.next_Node = None#pointer
		self.prev = None


#function
	def getData(self):
		return self.data

	def getNext_Data(self):
		return self.next_Node

	def setData(self,newdata):
		self.data - newdata

	def setNext_Data(self,newnext):
		self.next_Node = newnext

#new class for linked list
class MyLinked_List(object):
	def __init__(self):
		self.head = None


#funtion

	def add(self,item):
		new_node = Node(item)
		new_node.setNext_Data(self.head)
		new_node = self.head

	def printlist(self):
		current = self.head
		while current != None:
			print(current.data)
			current = current.next_Node

	def isEmpty(self):
		return self.head == None

	def size(self):
		current = self.head
		count = 0
		while current != None:
			count += 1
			current = current.getNext_Data()
		return count

	def search(self,item):
		current = self.head
		found = False
		while current != None and not found:
			if current.getData() == item:
				found = True
			else:
				current = current.getNext_Data()
		return found

	def remove(self,item):
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


while True:
	print("++++++++++++++++++++++++++++++++++++++++++++++++++++++")
	print("")
	print("1.create list")
	print("2.add node")
	print("3.remove node")
	print("4.size linked list")
	print("5.display")
	print("6.exit")
	print("")
	print("++++++++++++++++++++++++++++++++++++++++++++++++++++++")

	choice = int(input("enter your choice = "))

	if choice == 1:
		my_list = MyLinked_List()
		print("list has being created")
	elif choice == 2:
		item = int(input("enter number u want to add = "))
		my_list.add(item)
	elif choice == 3:
		item = int(input("enter the number u want to remove = "))
		my_list.remove(item)
	elif choice == 4:
		print("the size of the list is = ")
		my_list.size()
	elif choice == 5:
		print("the element in the list is = ")
		my_list.printlist()
	else:
		break'''


class node(object):
	def __init__(self,data=None):
		self.data=data
		self.next=None

class linked_list(object):
	def __init__(self):
		self.head=node()

	# Adds new node containing 'data' to the end of the linked list.
	def append(self,data):
		new_node=node(data)
		cur=self.head
		while cur.next!=None:
			cur=cur.next
		cur.next=new_node

	# Returns the length (integer) of the linked list.
	def length(self):
		cur=self.head
		total=0
		while cur.next!=None:
			total+=1
			cur=cur.next
		print(total)
		return total 


	# Prints out the linked list in traditional Python list format. 
	def display(self):
		elems=[]
		cur_node=self.head
		while cur_node.next!=None:
			cur_node=cur_node.next
			elems.append(cur_node.data)
		print(elems)

	# Returns the value of the node at 'index'. 
	def get(self,index):
		if index>=self.length():
			print("ERROR: 'Get' Index out of range!")
			return None
		cur_idx=0
		cur_node=self.head
		while True:
			cur_node=cur_node.next
			if cur_idx==index: return cur_node.data
			cur_idx+=1

	# Deletes the node at index 'index'.
	def erase(self,index):
		if index>=self.length():
			print("ERROR: 'Erase' Index out of range!")
			return 
		cur_idx=0
		cur_node=self.head
		while True:
			last_node=cur_node
			cur_node=cur_node.next
			if cur_idx==index:
				last_node.next=cur_node.next
				return
			cur_idx+=1

	


my_list=linked_list()
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.display()
my_list.length()











		


