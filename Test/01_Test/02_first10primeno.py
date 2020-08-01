n=10
x=2
while(n):
    for i in range(2, n):
        if n % i==0:
            break
        if i==x:
            print("First 10 prime is %d" %x)
            n=n-1
        x=x+1