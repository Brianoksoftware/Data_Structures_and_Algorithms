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
