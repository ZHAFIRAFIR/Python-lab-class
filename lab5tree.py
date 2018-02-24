class BinaryTree():
	def __init__(self, rootid):
		self.left = None
		self.right=None
		self.rootid=rootid

	def getleftchild(self):
		return self.left

	def getrightchild(self):
		return self.right

	def setNodeValue(self,value):
		self.rootid=value

	def getNodeValue(self):
		return self.rootid


	def insertRight(self,newNode):
		if myTree.right==None:
			myTree.right=BinaryTree(newNode)

		else:
			tree=BinaryTree(newNode)
			tree.right=myTree.right
			myTree.right=tree

	def insertLeft(self,newNode):
		if myTree.left==None:
			myTree.left=BinaryTree(newNode)

		else:
			tree=BinaryTree(newNode)
			tree.left=myTree.left
			myTree.left=tree

def printTree(tree):#left root right
	if tree != None:
		printTree(tree.getleftchild())
		print(tree.getNodeValue())
		printTree(tree.getrightchild())

myTree=BinaryTree("alya")
myTree.insertLeft("ben")
myTree.insertLeft("amir")
myTree.insertRight("amar")
myTree.insertRight("tamee")
myTree.insertRight("izati")

printTree(myTree)

		