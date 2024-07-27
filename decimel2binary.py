'''program to convert decimal to binary number'''

def dtobin(num):
    if num>=1:
        dtobin(num//2)
        print(num%2 ,end='')
dtobin(234)

def decimalToBinary(n): 
    return bin(n).replace("0b", "") 

#direct bin func
decNum = 4785
print(bin(decNum)[2:])#part of the code removes the 0b prefix from the binary string