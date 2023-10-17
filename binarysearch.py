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
    
   
    
  
  
