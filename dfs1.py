graph={
	'a':['b','c'],
	'b':['a','c','e'],
	'c':['a','b'],
	'd':['a','e','f'],
	'e':['b','d'],
	'f':['d']
}

def dfs(graph,node,visited):
	if node not in visited:
		visited.append(node)
		for n in graph(node):
			dfs(graph,n,visited)
	return visited

visited=dfs(graph,'a',[])
print(visited)