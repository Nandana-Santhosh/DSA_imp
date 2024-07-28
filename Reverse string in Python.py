'''Reverse string in Python'''

# 1st approach
def reverse(string):
    str=''
    for  i in string:
        str=i+str
    return str
print(reverse("Mango"))

#2nd approach
def reverse(s):
    if len(s)==0:
        return s
    else:
        return reverse(s[1:])+s[0]
s="APPLE"
print(reverse(s))