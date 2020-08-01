A =int(input("Enter the no: "))
B =int(input("Enter the another no"))
c = 0
x = A ^ B
while(x):
    c = c + (x & 1)
    x = x >> 1
print("no of bits flipped will be : %d" %x)