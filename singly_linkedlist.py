#Linked list data structure(singly linked list)
class Node:
    def __init__(self, data):
        self.data = data
        self.link = None

class Linkedlist:
    def __init__(self):
        self.head = None
    
    def insertFront(self, data):
        newnode = Node(data)
        newnode.link = self.head
        self.head = newnode
    
    def insertEnd(self, data):
        newnod = Node(data)
        if self.head == None:
            self.head = newnod
        else:
            current = self.head
            while current.link != None:
                current = current.link
            current.link = newnod
            
    def printOut(self):
        if self.head == None:
            print("Linked list empty!")
        else:
            current = self.head
            while current != None:
                print(current.data, end="->")
                current = current.link
            print("none")

llobj = Linkedlist()

llobj.insertEnd(10)
llobj.insertEnd(20)
llobj.insertEnd(30)
llobj.insertFront(9)


#Singly linked list...second example
class Node:
    def __init__(self,data):
        self.data = data
        self.link = None
        
class Linkedlist:
    def __init__(self):
        self.head = None
        
    def insertStart(self, data):
        newnode = Node(data)
        newnode.link = self.head
        self.head = newnode

    def insertEnd(self, data):
        newnodez = Node(data)
        if self.head is  None:
            self.head = newnodez
        else:
            current = self.head
            while current.link != None:
                current = current.link
            current.link = newnodez
        
    def printOut(self):
        if self.head == None:
            print("Linked list empty!")
        else:
            current = self.head
            while current != None:
                print(current.data, end="->")
                current = current.link
            print("None")

llobj = Linkedlist()
llobj.printOut()
llobj.insertStart(5)
llobj.printOut()
print("---------------------")

llobj.insertStart(3)
llobj.insertStart(1)
llobj.insertEnd(7)
llobj.insertEnd(9)
llobj.printOut()

'''
Singly linked list data structure EXAMPLE with 
methods to insert nodes at front & end of Linked list
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.link = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def insertMwanzo(self,data): #insertFront
        nodempya = Node(data)
        nodempya.link = self.head
        self.head = nodempya

    def insertMwisho(self, data): #insertEnd
        nodemanyien = Node(data)
        current = self.head
        while current.link != None:
            current = current.link
        current.link = nodemanyien

    def printer(self):
        if self.head == None:
            print("Linked list is EMPTY!")
        else:
            current = self.head
            while current != None:
                print(current.data, end="->")
                current = current.link
            print("None")

llistobj = Linkedlist()
llistobj.printer()

llistobj.insertMwanzo(4)
llistobj.insertMwanzo(3)
llistobj.insertMwanzo(1)
llistobj.printer()

llistobj.insertMwisho(6)
llistobj.insertMwisho(8)
llistobj.insertMwisho(10)
llistobj.printer()


'''
Singly linked list data structure EXAMPLE with 
methods to insert nodes at front & end of Linked list...FINAL IMPLEMENTATION
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.link = None
        
class Linkedlist:
    def __init__(self):
        self.head = None

    def display(self):
        if self.head == None:
            print("LINKED LIST EMPTY!")
        else:
            current = self.head
            while current != None:
                print(current.data, end="->")
                current = current.link 
            print("None")

    def addFront(self, data):
        nohde = Node(data)
        nohde.link = self.head
        self.head = nohde

    def addEnd(self, data):
        nohdeh = Node(data)
        current = self.head
        while current.link != None:
            current = current.link 
        current.link = nohdeh

llist = Linkedlist()        
llist.display()

llist.addFront(4)
llist.addFront(3)
llist.addFront(1)
llist.display()

llist.addEnd(5)
llist.addEnd(7)
llist.addEnd(9)
llist.display()



#Another singly linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.link  = None
    
class Linkedlist:
    def __init__(self):
        self.headNode = None
    
    def printerr(self):
        
        if self.headNode == None:
            print("Linked list empty!")
        else:
            currentNode = self.headNode
            while currentNode != None:
                print(currentNode.data, end="->")
                currentNode = currentNode.link
            print("None")
            
    def insertFront(self, data):
        newnode = Node(data)
        newnode.link = self.headNode
        self.headNode = newnode
    
    def insertEnd(self, data):
        newnode = Node(data)
        currentNode = self.headNode
        
        while currentNode.link != None:
            currentNode = currentNode.link 
        currentNode.link = newnode
            

llist = Linkedlist()
llist.printerr()
llist.insertFront(5)
llist.insertFront(3)
llist.insertFront(1)

llist.insertEnd(6)
llist.insertEnd(7)
llist.insertEnd(8)
llist.printerr()

#Another Singly linked list data structure implemented iteratively
class Node:
  def __init__(self, data):
    self.data = data
    self.link = None

class Linkedlist:
  def __init__(self):
    self.headnode = None

  def display(self):
    if self.headnode == None:
      print("Linked list empty!")
    currentnode = self.headnode
    while currentnode != None:
      print(currentnode.data, end="->")
      currentnode = currentnode.link
    print("None")
  
  def addFront(self, data):
    node = Node(data)
    node.link = self.headnode
    self.headnode = node

  def addEnd(self, data):
    newnode = Node(data)
    currentnode = self.headnode
    while currentnode.link != None:
      currentnode = currentnode.link
    currentnode.link = newnode


llist = Linkedlist()
llist.addFront(3)
llist.addFront(2)
llist.addFront(1)

llist.addEnd(4)
llist.addEnd(5)
llist.addEnd(6)

llist.display()


#Iterative singly linkedlist
class Node:
	def __init__(self, data):
		self.data = data
		self.link = None 

class Linkedlist:
	def __init__(self):
		self.headnode = None 

	def printerrr(self):
		if self.headnode is None:
			print("Linked list empty!")
		currentnode = self.headnode
		while currentnode is not None:
			print(currentnode.data, end="->")
			currentnode = currentnode.link 
		print("None")

	def insertStart(self, data):
		node = Node(data)
		node.link = self.headnode
		self.headnode = node

	def insertEnd(self, data):
		newnode = Node(data)
		currentnode = self.headnode
		while currentnode.link is not None:
		 	currentnode = currentnode.link
		currentnode.link = newnode


llist = Linkedlist()
llist.insertStart(3)
llist.insertStart(2)
llist.insertStart(1)

llist.insertEnd(4)
llist.insertEnd(5)
llist.insertEnd(6)
llist.insertEnd(7)
llist.printerrr()


			





            
            
        
        
        
        
        
        
         


