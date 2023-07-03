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


#Singly linked list
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

    def printOut(self):
        if self.head == None:
            print("Linked list empty!)
        else:
            current = self.head
            while current != None:
                print(current.data, end="->")
            
        
        
        
        
        
        
         




















llobj.printOut() 
