#WAP to count no of pairs in an array whose sum is equal to 30
arr= []
c=0
n= int(input("Enter size of array"))
print("Enter elements of array")
for i in range(n):
    x=int(input())
    arr.append(x)
for i in range(n):
    for j in range(1, n):
        if(arr[i]+arr[j]==30):
            c=c+1
print("No of pairs is: %d" %c)

