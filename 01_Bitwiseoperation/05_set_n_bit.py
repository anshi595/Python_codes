#WAP to set n no of bit from a given position
no= int(input("Enter the no"))
y= int(input("Enter starting bit"))
i= int(input("enter the no of bit to set"))


def set_n_bit(no, y, i):
    x=y-1
    while(x<y-1+i):
        no= ((1<<x) | no)
        x=x+1
    return no
f= set_n_bit(no, y, i)
print(f)