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

#pop operation/remove last item in the stack
remove_last = stack_list.pop()
print("Last item removed:", remove_last)
print("Current list:", stack_list)

#peak operation
element_check = stack_list[-1]
print("Last item in stack now:", element_check)
print("Current list:", stack_list)
