def arrange(s):
    z=""
    o=""
    t=""
    for i in s:
        if i=="1":
            o+="1"
        elif i=="2":
            t+="2"
        elif i=="0":
            z+="0"
    print(o+z+t)
s=input().strip()
arrange(s)





def arrange(s):
    ones = []
    zeros = []
    twos = []
    
    for i in s:
        if i == "1":
            ones.append("1")
        elif i == "2":
            twos.append("2")
        else:
            zeros.append("0")

    print("".join(ones + zeros + twos))  # Efficient concatenation

s = input().strip()
arrange(s)

