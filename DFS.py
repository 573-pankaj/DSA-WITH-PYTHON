class Tree:
	def __init__(self,data,left=None,right=None):
		self.data = data
		self.right = right
		self.left = left
	
def dfsPreorder(root):
	if root is None:
		return
	else:
		print(root.data)
		dfsPreorder(root.left)
		dfsPreorder(root.right)

def dfsInorder(root):
	if root is None:
		return
	else:
		dfsInorder(root.left)
		print(root)
		dfsInorder(root.right)

def dfsPostorder(root):
	if root is None:
		return
	else:
		dfsPostorder(data.left)
		dfsPostorder(data.right)
		print(root)

