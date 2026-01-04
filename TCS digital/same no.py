n=int(input())
li=list(map(int,input().split()[:n])) # taking input array with fixed size
m=li[0]
c=0
for i in range(n):
    if li[i]!=m:
        c+=1

print(c)
