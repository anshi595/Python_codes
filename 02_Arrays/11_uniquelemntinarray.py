#WAP to check if the array has unique elements
arr= []
y= []
n= int(input("Enter size of array"))
print("Enter elements of array")
for i in range(n):
    x=int(input())
    arr.append(x)

y= set(arr)
if(len(arr)==len(y)):
    print("Unique")
else:
    print("Not unique")



