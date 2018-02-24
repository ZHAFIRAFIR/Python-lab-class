class Graph(object):
	"""docstring for Graph"""
	def __init__(self):
		
		self.vertex={}

	def insert_vertex(self,v):
		self.vertex[v]=[]

	def insert_edge(self,u,v,e):
		self.vertex[u].append(e)
		self.vertex[v].append(e)

	def print_adjacencylist(self):
		print("adjacency list")
		for i in self.vertex:
			print(i,':',self.vertex[i])
			

grapobj=Graph()


while True:
	print("#######################################")
	print(" ")
	print("1. insert vertex")
	print("2. indert edge")
	print("3. Display")
	print("4. choose source node ")
	print("5. Exit")
	print("#######################################")

	choice=int(input("ENTER YOUR CHOICE : "))

	if choice==1:
		item=int(input("insert  vertex:"))
		grapobj.insert_vertex(item)
	elif choice==2:
		number=int(input("insert edge: "))
		grapobj.insert_edge(number)
	elif choice==3:
		grapobj.print_adjacencylist()
	elif choice==4:
		break
	elif choice == 5:
		break

	else:
		print("wrong choice!!")	


