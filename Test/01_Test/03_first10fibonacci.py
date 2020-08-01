n=int(input("Enter the no"))
fib1=0
fib2=1
print(fib1)
print(fib2)
if n>=2:
    for i in range(2, n):
        fib=fib1+fib2
        fib1=fib2
        fib2=fib
        print(fib)

