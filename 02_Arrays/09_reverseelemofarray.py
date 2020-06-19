#WAP to reverse all the elements of an array
arr= []
n= int(input("Enter size of array"))
print("Enter elements of array")
for i in range(n):
    x=int(input())
    arr.append(x)
arr.reverse()
print(arr)
