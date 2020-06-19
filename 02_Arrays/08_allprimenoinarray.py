def isprime(n):
    c=0
    for i in range(2, n):
        if ( n % 2 == 0):
                c = 1
                break
    if(n==1):
        print("1 is not prime")
    elif(c==0):
        return print(n, " is a prime no")
    else:
        return print(n,  " is not a prime no ")


arr= []
n = int(input("Enter size of array"))
print("Enter elements of array")
for i in range(n):
    x = int(input())
    arr.append(x)
for i in range(n):
    isprime(arr[i])




