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


myGraph=Graph()
myGraph.insert_vertex("koe")
myGraph.insert_vertex("kict")
myGraph.insert_vertex("knms")
myGraph.insert_vertex("Irkhs")

myGraph.insert_edge("koe","kict","a")
myGraph.insert_edge("koe","knms","b")
myGraph.insert_edge("koe","Irkhs","c")

myGraph.print_adjacencylist()