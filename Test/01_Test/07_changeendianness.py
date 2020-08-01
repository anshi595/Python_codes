def ChangeEndian(n):
    byte0= (n & 0x000000FF)  << 24
    byte1= (n & 0x0000FF00)  << 8
    byte2= (n & 0x00FF0000)  << 8
    byte3= (n & 0xFF000000)  << 24

    return byte0 | byte1 | byte2 | byte3

n=int(input("Enter the no:"))
print("The no after changing endianness is: %x " %ChangeEndian(n))
