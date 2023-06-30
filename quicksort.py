#Quicksort algorithm implemented recursively
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
