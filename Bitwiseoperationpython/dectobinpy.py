def dectobin(n):
    for i in range(31, -1, -1):
        k= n >> i
        if(k & 1):
            print(1,  end= "")
        else:
            print(0, end= "")
n= int(input())
p= dectobin(n)

        
        