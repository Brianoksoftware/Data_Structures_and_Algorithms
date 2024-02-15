#Factorial finder python
n = int(input("Enter a number whose factorial you want:"))

def factorial(n):
  if n < 0:
    print("ERROR. Enter whole number!")
  elif n < 2:
    return 1
  else:
    return n * factorial(n - 1)
print(f"The factorial of {n} is:", factorial(n))


#Another factorial example using recursion
n = int(input("Enter a number to calculate it's factorial:"))

def find_factorial(n):
  if n < 0:
    prrint("Enter a non-negative number!")
  elif n < 2:
    return 1
  else:
    return n * find_factorial(n - 1)

print(f"Factorial of {n} is:", find_factorial(n))


#Factorial finder function using recursion
n = int(input("Enter an integer to calculate it's factorial:"))
def factorialx(n):
  if n < 2:
    return 1 
  else:
    return n * factorialx(n - 1)

print(f"The factorial of {n} is:", factorialx(n))


n =3
def facto(n):
	if n < 2:
		return 1
	else:
		return n * facto(n - 1)

print(facto(n))
