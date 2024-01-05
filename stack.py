'''
Stack data structure...last in, first out(LIFO)
Implementation using lists
'''
stack_list = []
print("Current list:", stack_list)

#push/append operation
stack_list.append(5)
stack_list.append(6)
stack_list.append(7)
print("New list:", stack_list)

#pop operation/remove last item in the stack,check if stack is empty first
if len(stack_list) == 0:
	print("error")
else:
	remove_last = stack_list.pop()
print("Last item removed:", remove_last)
print("Current list:", stack_list)

#peek operation,check if stack is empty first

if len(stack_list) == 0:
	print("error")
else:
	element_check = stack_list[-1]

print("Last item in stack now:", element_check)
print("Current list:", stack_list)



'''
Stack data structure...last in, first out(LIFO)
Implementation using classes & OOP
'''
class Stack:
	def __init__(self):
		self.stack =[]

	def push(self, element):
		self.stack.append(element)

	def pop(self): #insertion operation
		if self.is_empty():
			print("Stack empty!")
		else:
			return self.stack.pop()

	def peek(self):
		if not self.is_empty():
			return self.stack[-1]
		else:
			print("Stack empty!")

	def is_empty(self):
		return len(self.stack) == 0

	def __str__(self): #The __str__ method allows you to define a human-readable string representation of your class. 
		return str(self.stack)


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(35)

print("New stack:", stack)
print("Last element:", stack.peek())

stack.pop()
print("New stack:", stack)
print("Last element:", stack.peek())


'''
Stack implementation using lists (LIFO)
'''
#Creating stack
stack = []
#Populating stack
stack.append(2)
stack.append(1)
stack.append(0)
print("Stack:", stack)
#Pop operation...first check if stack is empty
if len(stack) == 0:
	print("Error")
else:
	stack.pop()
	print("New Stack:", stack)
#Peek operation...first check if stack is empty
if len(stack) == 0:
	print("Error")
else:
	peeked = stack[-1]
	print("Peeked/last item:", peeked)




