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
Final singly linked list data structure EXAMPLE with 
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



            
            
        
        
        
        
        
        
         


