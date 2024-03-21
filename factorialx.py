n = int(input("Enter a positive integer:"))

def facto(n):
    if n < 0:
        #print("Undefined!")
        return
    elif n < 2:
        return 1
    else:
        return n * facto(n - 1)

print(f"Factorial of {n} is:", facto(n))
