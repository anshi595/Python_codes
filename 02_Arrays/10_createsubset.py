# Q 10 WAP to create subset from an array
arr= []
y= []
n= int(input("Enter size of array"))
print("Enter elements of array")
for i in range(n):
    x=int(input())
    arr.append(x)

y= set(arr)
type(y)
print(y)