'''
Binary search implemented iteratively in python
NOTE: Iterative binary search is more efficient than recursive binary search especially for large datasets
'''
def binary_search(arr, item):
  start_index = 0
  stop_index = len(arr) - 1
  
  while start_index <= stop_index:
    midpoint = start_index + (stop_index - start_index) // 2
    midpoint_value = arr[midpoint]

    if midpoint_value == item:
      return midpoint

    elif item < midpoint_value:
        stop_index = midpoint - 1

    else:
      stop_index = midpoint + 1

  return None

#arr = [4,2,1,5,7,3]
#arr = [4,2,5]
#arr_sorted = sorted(arr)
#arr = [4,2,1,5,7,3]
arr = [1,2,3,4,5,7]
item = 2

#print("Item is at position:", binary_search(arr_sorted, item))
print("Item is at position:", binary_search(arr, item))

#Another binary seach example
def binarysearch(arr, target_value):
	lower_bound = 0
	upper_bound = len(arr) - 1

	while lower_bound <= upper_bound:
		midpoint_index = (lower_bound + upper_bound) //2

		if arr[midpoint_index] == target_value:
			return midpoint_index #Return the index where the target value is
		elif arr[midpoint_index] < target_value:
			lower_bound = midpoint_index + 1 #Update lower bound
		else:
			upper_bound = midpoint_index - 1 #Update upper bound
	return None #if target value not in array

arr = [1,3,5,6,7]
target_value = 0
print(f"Target value {target_value} at position:", binarysearch(arr, target_value))


#Binary search algorithm...implemented recursively
target = 3
def binarysearch(arr, target, low, high):
	if low <= high:
		midpoint = (low + high) // 2

		if arr[midpoint] == target:
			return midpoint
		elif arr[midpoint] > target:
			return binarysearch(arr, target, low, midpoint - 1)
		else:
			return binarysearch(arr, target, midpoint + 1, high)
	return None

print(f"The target value:{target} is at index:", binarysearch([1,2,3,4], target,1,4))



#Binary search...implemented recursively
target = 3
array = [3,1,4,2]
sorted_array = sorted(array) #sorted_array = [1,2,3,4]
def binarysearch(arr, target, low, high):
	if low <= high:
		midpoint = (low + high) // 2

		if arr[midpoint] == target:
			return midpoint
		elif arr[midpoint] > target:
			return binarysearch(arr, target, low, midpoint - 1)
		else:
			return binarysearch(arr, target, midpoint + 1, high)
	return None

print(f"The target value:{target} is at index:", binarysearch([1,2,3,4], target,1,4))



#Binary search implemented recursively
arr = sorted([4,1,3,2,5])
#arr = [1,2,3,4,5]
target_value = 5
lower_bound = 0
higher_bound = len(arr) - 1

def binary_search(arr, target_value, lower_bound, higher_bound):
	if lower_bound <= higher_bound:
		midpoint = (lower_bound + higher_bound) // 2
		if arr[midpoint] == target_value:
			return midpoint
		elif arr[midpoint] < target_value:
			return binary_search(arr, target_value, midpoint + 1, higher_bound )
		else:
			return binary_search(arr, target_value, lower_bound, midpoint -1 )
	return None

print(f"The value: {target_value} is at index:{binary_search(arr, target_value, lower_bound, higher_bound)}")



#Binary search algorithm implemented recursively
unsorted_array = [2,5,1,4,3]
arr = sorted(unsorted_array) #arr =[1,2,3,4,5]
lower = 0
target_value = 1
higher = len(arr) - 1

def binarysearch(arr, target_value, lower, higher):
	if lower <= higher:
		midpoint_index = (lower + higher) // 2

		if arr[midpoint_index] == target_value:
			return midpoint_index

		elif arr[midpoint_index] > target_value:
			return binarysearch(arr, target_value, lower, midpoint_index - 1)
		else:
			return binarysearch(arr, target_value, midpoint_index + 1, higher)

	else:
		return None

print(f"The target value:{target_value} is at index:{binarysearch(arr, target_value, lower, higher)}")

   
    
  
  
