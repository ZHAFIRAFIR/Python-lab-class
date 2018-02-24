V= int(input("number of node:"))
E= int(input("number of edge:"))

adj_matrix =[]

for i in range(0,V):
	temp = [0]*V
	adj_matrix,append(temp)

print("Enter two connected vertices and the connecting edge (eg: node1 node2 weight):")

for i in range(0,E):
	S=input()
	U,v,
	U=int(U)
	v=int(V)
	W=(W)
	adj_matrix[V][U]= adj_matrix[U][v]=W

	print("/n the adjacency matrix")
	print("__",end="")
	for i in range(0,v):
		print(i,end="__")
	print("/n")

	for i in range(0,V):
		print(i,end="")
		for j in adj_matrix[i]:
			print(j,end="  ")
		print("/n")



