graph1={
	'A':['B','C'],
	'B':['A','C','E'],
	'C':['A','B'],
	'D':['A','E','F'],
	'E':['B','D'],
	'F':['D']


}

def dfs(graph,node,visited):
	if node not in visited:
		visited.ppend(node)
		for n in graph[node]:
			dfs(graph,n,visited)
	return visited

visited= dfs(graph1,"C",[])
print(visited)


