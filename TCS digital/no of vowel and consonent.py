s=str(input())
vowel=['A','E','I','O','U','a','e','i','o','u']
v=0
c=0
for i in s:
    if i in vowel and i.isalpha():
        v+=1
    elif i not in vowel and i.isalpha():
        c+=1
print(v,c)