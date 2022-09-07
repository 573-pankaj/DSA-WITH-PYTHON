class Node:  # 1st class here is node class
	def __init__(self,data=None,next=None): # constructor
		self.data = data    # here difine two class members 
		self.next = next  #next which is the pointer two the next elements

class LinkedList: # 2nd class is LinkedList class
	def __init__(self): # constructor
		self.head = None # its points head of the linked list

	def insert_at_begining(self,data): # class member function # insert at the begging of the linked List 
		node = Node(data, self.head)  # creating a node , which value is data 
		self.head = node # current head is now 'node'

	def print(self): # utility function
		if self.head is None:
			print("Linked List is Empty")
			return
		itr = self.head # temporary variable
		listr = '' # string
		while itr: # So you are now flowwing the link in your link, lister, trading through element one by one
			listr += str(itr.data) + '-->'
			itr = itr.next
		print(listr)


	def insert_at_end(self,data):
		if self.head is None:
			self.head = Node(data,None)
			return

		itr = self.head
		while itr.next:
			itr = itr.next

		itr.next = Node(data, None)




if __name__ == '__main__': 
	lr = LinkedList()
	lr.insert_at_begining(5)
	lr.insert_at_begining(89)
	lr.insert_at_end(77)
	
	lr.print()

	#lr.insert_at_begining(23)
	#lr.insert_at_begining(33)
	#lr.insert_at_begining(44)