# Q-6 Merge two array in third array
arr1= []
n1= int(input("Enter size of array"))
print("Enter elements of array")
for i in range(n1):
    x=int(input())
    arr1.append(x)
arr2= []
n2= int(input("Enter size of array"))
print("Enter elements of array")
for i in range(n2):
    x=int(input())
    arr2.append(x)
arr3= arr1 + arr2
print(arr3)
