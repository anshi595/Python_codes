n=int(input("Enter the no"))
rn=0
while(n!=0):
    rem= n % 10
    n= n // 10
    rn= rn * 10 + rem
print("Reversed no is: %d " %rn)