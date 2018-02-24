queue=[]

def enqueue(item):
	queue.append(item)

def dequeue():
	queue.pop(0)

def size():
	return len(queue)

def isEmpty():
	if queue ==[]:
		print("the queue is empty")
	else:
		print("the queue is not empty")

def printQ():
	for element in queue:
		print(element)

while True:
	print("++++++++++++++++++++")
	print("1.enqueue")
	print("2.dequeue")
	print("3.size")
	print("4.isEmpty")
	print("5.display")
	print("6.exit")
	print("++++++++++++++++++++")

	choice=int(input("enter your choice:"))

	if choice==1:
		number=int(input("enter the number to be enqueue:"))
		enqueue(number)
	elif choice==2:
		dequeue()
	elif choice==3:
		print("size of queue is",size())
	elif choice==4:
		isEmpty()
	elif choice==5:
		printQ()
	else:
		break
