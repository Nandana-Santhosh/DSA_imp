'''Remove Duplicate from an array'''

li=[1,2,6,4,7,3,1,6]
new=[]
for i in li:
    if i not in new:
        new.append(i)
    else:
        i+=1
print(new)
print(set(li))
