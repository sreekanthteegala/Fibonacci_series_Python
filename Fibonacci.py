import math
n=list(map(int,input("Enter the numbers separated by ',': ").split(",")))
def isPerfectSquare(x):
    s = int(math.sqrt(x))
    return s*s == x
def isFibonacci(b):
    return isPerfectSquare(5*b*b + 4) or isPerfectSquare(5*b*b - 4)
for i in (n):
    if (isFibonacci(i) == True):
        print(i, "is valid")
    else:
        print(i, "is not valid")

# nothing
