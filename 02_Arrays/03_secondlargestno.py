#WAP to find the second largest no in an array
arr= []
n= int(input("Enter size of array"))
print("Enter elements of array")
for i in range(n):
    x=int(input())
    arr.append(x)
max1=max2=arr[0]
for i in range(1, n):
    if(arr[i]>max1):
        max2=max1
        max1=arr[i]
    elif(max2 > arr[i] and arr[i] < max1):
        max2 = arr[i]
print(max2)
