#Quicksort algorithm implemented recursively...choosing middle element as pivot
def quick_sort(arr):
	if len(arr) <=1:
		return arr
	else:
		pivot = arr[len(arr)//2]
		lesser = []
		greater = [] 

		for i in range(len(arr)):
			if arr[i] < pivot:
				lesser.append(arr[i])
			elif arr[i] > pivot:
				greater.append(arr[i])
		return quick_sort(lesser) + [pivot] + quick_sort(greater)
print("Quicksorted:", quick_sort([5,2,3,1,4,0]))


#Quicksort algorithm implemented recursively...an implementation involving choosing the pivot randomly
import random

def quicksort(arr):
	if len(arr) <= 1:
		return arr 
	else:
		pivot = random.choice(arr)
		lesser = []
		greater = []

		for elem in range(len(arr)):
			if arr[elem] < pivot:
				lesser.append(arr[elem])
			elif arr[elem] > pivot:
				greater.append(arr[elem])

		return quicksort(lesser) + [pivot] + quicksort(greater)

print("sorted list:", quicksort([5,3,9,0,2,4,1,6,8,7]))


