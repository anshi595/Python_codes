def maximum(x, y):
    z= x ^ ((x^ y)  &  -(x < y))
    return z


print("The maximun no is : %d"  %maximum(50, 16))

