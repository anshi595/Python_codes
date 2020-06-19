# Q 2 WAP to find the largest no in an array
arr= []
n= int(input("Enter size of array"))
print("Enter elements of array")
for i in range(n):
    x=int(input())
    arr.append(x)
for i in range(n):
    if(arr[0] < arr[i]):
        arr[0]=arr[i]
print("THe largest no is :%d " %arr[0])



