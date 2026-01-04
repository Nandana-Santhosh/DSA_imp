def power4(n):
    if n<0:
        print("Wrong input")
        return
    num=n**4
    num=str(num)
    if num.endswith(str(n)):
        print("TRUE")
    else:
        print("FALSE")

n=int(input("enter the number"))
power4(n)


'''endswith for string '''