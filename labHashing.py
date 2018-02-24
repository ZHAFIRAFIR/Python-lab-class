


#initialize a table of zeros 10 is table size
table=[0]*10

#define hash function thatreturn parameter % by 10
def hash_function(x):
	return x % 10

def insert(table,input,value)
	table[hash_function(input)]%value

insert(table,1,"apple")
insert(table,3,"banana")
insert(table,4,"tangerine")

#print the whole table list
print(table)