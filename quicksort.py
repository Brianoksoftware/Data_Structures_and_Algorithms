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


#quicksort algorithm in python using recursion...mastery 1
arr = [6,5,4,3,2,1]

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    #Middle index as pivot...value floored
    pivot = arr[len(arr)//2]
    lessr = []
    greatr = []
    
    for i in range(len(arr)):
        if arr[i] < pivot:
            lessr.append(arr[i])
        elif arr[i] > pivot:
            greatr.append(arr[i])
    return quicksort(lessr) + [pivot] + quicksort(greatr)

print("Quicksorted list:", quicksort(arr))


#Another quicksort implemented recursively
arry = [5,2,1,3,4]
def quick_sort(arry):
	if len(arry) <= 1:
		return arry
	pivot = arry[len(arry)//2]
	lesser = []
	greater = []
	
	for i in range(len(arry)):
		if arry[i] < pivot:
			lesser.append(arry[i])
		elif arry[i] > pivot:
			greater.append(arry[i])
	return quick_sort(lesser) + [pivot] + quick_sort(greater)

print("Quicksorted list:", quick_sort(arry))




#Quicksort implemented recursively...takes integers from user and uses them to populate list arry
arry = []
for i in range(5):
	inputt = int(input("Enter a number:"))
	arry.append(inputt)
	
def quick_sort(arry):
	if len(arry) <= 1:
		return arry
	pivot = arry[len(arry)//2]
	lesser = []
	greater = []
	
	for i in range(len(arry)):
		if arry[i] < pivot:
			lesser.append(arry[i])
		elif arry[i] > pivot:
			greater.append(arry[i])
	return quick_sort(lesser) + [pivot] + quick_sort(greater)

print("Quicksorted list:", quick_sort(arry))



#Quicksort algorithm implemented recursively.
#It takes user input and uses the integers to populate a list
array = []

for x in range(5):
	y = int(input("Enter a number:"))
	array.append(y)

def quicksort(array):
	if len(array) <= 1:
		return array

	pivot = array[len(array)//2]
	lesser = []
	greater = []

	for index in range(len(array)):
		if array[index] < pivot:
			lesser.append(array[index])
		elif array[index] > pivot:
			greater.append(array[index])
	return quicksort(lesser) + [pivot] + quicksort(greater)

print("Quicksorted array:", quicksort(array))



#Quicksort...implemented recursively
arr = [6,5,2,9,1]

def quick_sort(arr):
	if len(arr) <= 1:
		return arr

	pivot = arr[len(arr) //2 ]
	lesser= []
	greater = []

	for elem in range(len(arr)):
		if arr[elem] < pivot:
			lesser.append(arr[elem])
		elif arr[elem] > pivot:
			greater.append(arr[elem])
	return quick_sort(lesser) + [pivot] + quick_sort(greater)

print("Quicksorted list:", quick_sort(arr))


#Quicksort algorithm implemented recursively
arry = [6,3,98,3903,4,2,9,4,1,0]

def quicksort(arry):
	if len(arry) <= 1:
		return arry
	pivot = arry[len(arry) // 2]
	lesser = []
	greater = []

	for elem in range(len(arry)):
		if arry[elem] < pivot:
			lesser.append(arry[elem])
		elif arry[elem] > pivot:
			greater.append(arry[elem])
			#skips over arry[elem] == pivot
	return quicksort(lesser) + quicksort([pivot]) + quicksort(greater)

print("Quicksorted array/list:", quicksort(arry))


#Another quicksort algorithm example implemented recursively
arr = [65,3,9,0,43,1,7,0]

def quicksorto(arr):
	if len(arr) <= 1:
		return arr
	pivot = arr[len(arr) // 2]
	lesser = []
	greater = []

	for item in range(len(arr)):
		if arr[item] < pivot:
			lesser.append(arr[item])
		elif arr[item] > pivot:
			greater.append(arr[item])
	return quicksorto(lesser) + [pivot] + quicksorto(greater)

print("Quicksorted array:", quicksorto(arr))







