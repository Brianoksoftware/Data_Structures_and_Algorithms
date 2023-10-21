#Implementation of a Queue data structure in python

class Queue:
	def __init__(self):
		self.items = []

	def is_empty(self):
		return self.items == 0

	def enqueue(self, element):
		self.items.append(element)

	def dequeue(self):
		if not self.is_empty():
			item = self.items.pop(0)
		else:
			print("Queue is empty!")
			return None #not necessary...python returns None automatically
	'''
	def peek(self): #peek operations are traditionally not done in queues
		if not self.is_empty():
			item = self.dequeue()
			self.enqueue(item)
			return item

		else:
			print("Can't 'peak' queue is empty!")
			return None
	'''

	def display(self):
		print("Queue:", self.items)

	#we can also use __str__
	def __str__(self):
		return str(self.items)

queue = Queue()

queue.display()
print()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

queue.display()
print()

queue.dequeue() #removes first element in first (FIFO)

queue.display()

