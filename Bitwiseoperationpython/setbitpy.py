def setbit(n):
    count=0
    for i in range(32):
        if((n & (1 << i)) == (1 << i)):
            count+=1
    return count
p= int(input())
x = setbit( p)
print("The no of set bit", x)

        
            