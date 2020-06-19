#WAP to count frequency of elements of an array
arr= []
n= int(input("Enter size of array"))
print("Enter elements of array")
for i in range(n):
    x=int(input())
    arr.append(x)
print(arr)
for i in range(n):
    print(arr.count(arr[i]))








