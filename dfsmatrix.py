v=int(input("number of node:"))
e=int(input("number of edge:"))

adj_matrix=[]

for i in range(0,v):
	temp=[0]*v
	adj_matrix.append(temp)
print("enter two connected verticle and the connecting edge(eg:node1 node2 weight:")
for i in range(0,e):
	s= input()
	u,v,w=s.split()
	u=int(u)
	v=int(v)
	w=(w)
	adj_matrix[v][u]=adj_matrix[u][v]=w

print("\nthe adj_matrix:")
print("_",end="")
for i in range(0,v):
	print(i,end="_")
print("\n|")

for i in range(0,v):
	print(i,end="|")
	for j in adj_matrix[i]:
		print(j,end='')
	print("\n|")
