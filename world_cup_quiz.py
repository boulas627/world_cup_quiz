

class Node: 
	def __init__(self, question, correct_answer, difficulty): 
		self.question = question 
		self.correct_answer = correct_answer
		self.left = None
		self.right = None

def insert(node, question, correct_answer, difficulty): 
	if node is None: 
		return Node(question, correct_answer, difficulty)

	if difficulty < node.difficulty: 
		node.left = insert(node.left, question, correct_answer, difficulty)

	else:
		node.right = insert(node.right, question, correct_answer, difficulty)

	return node 

def inorder(root): 
	if root is not None: 
		inorder(root.left)

		# Traverse root 
		print(root.question)

		# Traverse right 
		inorder(root.right)


root = None 

root = insert(root, "Which Confederation(s) have won world cups? ", "COMNEBOL and UEFA", 5)

print(inorder(root))