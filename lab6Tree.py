class Node(object):
	def __init__(self,info):
		self.info = info
		self.left = None
		self.right = None

	def __str__(self):
		return str(self.info)

class BSTtree(object):
	def __init__(self):
		self.root = None

	def create(self,value):
		if self.root == None:
			self.root = Node(value)

		else:
			current=self.root
			while 1:
				if value <current.info:
					if current.left:
						current = current.left
					else:
						current.left=Node(value)
						break;

				elif value > current.info:
					if current.right:
						current=current.right
					else:
						current.right=Node(value)
						break;

				else:
					break


	def inorder(self,node):
		if node is not None:
			self.inorder(node.left)
			print(node.info)
			self.inorder(node.right)

	def preorder(self,node):
		if node is not None:
			print(node.info)
			self.preorder(node.left)
			self.preorder(node.right)

	def postorder(self,node):
		if node is not None:
			self.postorder(node.left)
			self.postorder(node.right)
			print(node.info)

myTree = BSTtree()
Array=[8,3,1,6,4,7,10,14,13]

for i in Array:
	myTree.create(i)

print("data =",Array)
print("Inorder Traversal")
myTree.inorder(myTree.root)
print("preorder Traversal")
myTree.preorder(myTree.root)
print("postorder Traversal")
myTree.postorder(myTree.root)


