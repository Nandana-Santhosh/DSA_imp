'''Python Program to check if strings are rotations of each other or not'''

'''  1. Create a temp string and store concatenation of str1 to
       str1 in temp.
                          temp = str1.str1
    2. If str2 is a substring of temp then str1 and str2 are 
       rotations of each other.

    Example:                 
                     str1 = "ABACD"
                     str2 = "CDABA"

     temp = str1.str1 = "ABACDABACD"
     Since str2 is a substring of temp, str1 and str2 are 
     rotations of each other.'''

def arerotation(st1,st2):
    if len(st1)!=len(st2):
        return 0
    tem=''
    temp=st1+st2
    if temp.count(st2)>0:
        return 1
    else:
        return 0
print(arerotation("hello" ,"elohe"))
    