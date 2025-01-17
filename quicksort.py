#quicksort algorithm implemented recursively
arrz = [78,45,39,938,3,44,64,47]
def quicksorrt(arrz):
	if len(arrz) <=1:
		return arrz
	pivot = arrz[len(arrz)//2]
	lesser = []
	equal = []
	greater = []

	for y in range(len(arrz)):
		if arrz[y] < pivot:
			lesser.append(arrz[y])
		elif arrz[y] == pivot:
			equal.append(arrz[y])
		else:
			greater.append(arrz[y])
	return quicksorrt(lesser) + equal + quicksorrt(greater)

print("Quiksorted array/list:", quicksorrt(arrz))
print()






#quicksort algorithm implemented recursively in python
array = [2,7,8,17,98,4]
def qsort(array):
	if len(array) <=1:
		return array
	pivot = array[len(array)//2]
	lessr = []
	equal = []
	greater = []

	for z in range(len(array)):
		if array[z] < pivot:
			lessr.append(array[z])
		elif array[z] == pivot:
			equal.append(array[z])
		else:
			greater.append(array[z])

	return qsort(lessr) + equal + qsort(greater)

print("QUICKSORTED ARRAY:", qsort(array))
print()







#QUICKSORT ALGORITHYM implemented using recursion
arr = [6,3,7,9,2,0,1]
def qsort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr)//2]
        lesser = []
        equal = []
        greater = []
        
        for i in range(len(arr)):
            if(arr[i] < pivot):
                lesser.append(arr[i])
            elif arr[i] == pivot:
                equal.append(arr[i])
            else:
                greater.append(arr[i])
        
        return qsort(lesser) + equal + qsort(greater)

print("Quicksorted list:", qsort(arr))



arr = [5,545,8,4,97,2132,2,1,9]

def qsort(arr):
    if len(arr) <= 1:
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
        return qsort(lesser) + [pivot] + qsort(greater)

print("The quicksorted array:", qsort(arr))


arr = [6,9,3,0,24,67,2,1234]

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr)//2]
    lesser = []
    greater = []

    for i in range(len(arr)):
        if arr[i] < pivot:
            lesser.append(arr[i])
        elif arr[i] > pivot:
            greater.append(arr[i])
    return quicksort(lesser) + [pivot] + quicksort(greater)

print("Quicksorted list/array:", quicksort(arr))


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



#Quicksort algorithm...recursively
arr = [4,2,1,3,0]

def quicksort(arr):
	if len(arr) <= 1:
		return arr 

	pivot = arr[len(arr)//2]
	lesser = []
	greater = []

	for i in range(len(arr)):
		if arr[i] < pivot:
			lesser.append(arr[i])
		elif arr[i] > pivot:
			greater.append(arr[i])
	return quicksort(lesser) + [pivot] + quicksort(greater)

print("The Quicksorted list:", quicksort(arr))



arr=[78,4,8,2,7,9,2334]

def q_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    lessr = []
    greatr = []
   
    for i in range(len(arr)):
        if arr[i] < pivot:
            lessr.append(arr[i])
        elif arr[i] > pivot:
            greatr.append(arr[i])
    return q_sort(lessr) + [pivot] + q_sort(greatr)

print("Quicksorted array:", q_sort(arr))



arr4y = [8,9,1,4,7,0,2,6]

def quickssort(arr4y):
	if len(arr4y) <= 1:
		return arr4y
	pivot = arr4y[len(arr4y)//2]
	lessr = []
	greatr = []

	for item in range(len(arr4y)):
		if arr4y[item] < pivot:
			lessr.append(arr4y[item])
		elif arr4y[item] > pivot:
			greatr.append(arr4y[item])
	return quickssort(lessr) + [pivot] + quickssort(greatr)
print("Array after quicksort:", quickssort(arr4y))


#QUICKSORT ALGORITHYM
arr = [6,9,3,0,24,67,2,1234]

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr)//2]
    lesser = []
    greater = []

    for i in range(len(arr)):
        if arr[i] < pivot:
            lesser.append(arr[i])
        elif arr[i] > pivot:
            greater.append(arr[i])
    return quicksort(lesser) + [pivot] + quicksort(greater)

print("Quicksorted list/array:", quicksort(arr))
            
    

           



	





