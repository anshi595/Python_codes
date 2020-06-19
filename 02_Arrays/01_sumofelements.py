# Q1 WAP to calculate sum of elements of an array
arr=[]
n=input("Enter the size")
print("Enter array elements")
for i in range(int(n)):
    num=input()
    arr.append(int(num))
print("sum: %d" %sum(arr))


