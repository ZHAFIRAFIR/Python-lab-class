class Graph(object):
	"""docstring for graph"""
	def __init__(self):
		self.vertex={}

	def insert_vertex(self,v):
		self.vertex[v]={}

	def insert_edge(self,u,v,e):
		self.vertex[u].append(e)
		self.vertex[v].append(e)

	def print_adjacencyList(self):
		print("adjacency List")
		for i in self.vertex:
			print(i,':',self.vertex[i])

myGraph=Graph()
myGraph.insert_vertex("KOE")
myGraph.insert_vertex("KICT")
myGraph.insert_vertex("knms")
myGraph.insert_vertex("Irkhs")

myGraph.insert_edge("KOE","KICT","a")
myGraph.insert_edge("KOE","knms","b")
myGraph.insert_edge("KOE","Irkhs","c")

myGraph.print_adjacencyList()

		