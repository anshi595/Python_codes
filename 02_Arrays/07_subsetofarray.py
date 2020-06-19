# Q-7 Find if array A is subset of B
arr1= []
arr2= []
n1= int(input("Enter size of array1"))
print("Enter elements of array1")
for i in range(n1):
    x=int(input())
    arr1.append(x)
n2= int(input("Enter size of array2"))
print("Enter elements of array2")
for i in range(n2):
    x=int(input())
    arr2.append(x)
#y= set(arr1)
#z= set(arr2)
#p= print(y.issubset(z))
if(set(arr1).issubset(set(arr2))):
    print('Arr1 is subset of Arr2')
else:
    print("not a subset")


