n= int(input("Enter the no"))
x= int(input("Enter the bits to be rotated"))


def leftshift(n, x):
    a = (n << x)
    b = (n >> (32-x))
    return a | b


def rightshift(n, x):
    a = (n >> x)
    b = (n << (32-x))
    return a | b

print(leftshift(n, x))
print(rightshift(n, x))