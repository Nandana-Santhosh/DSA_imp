st=str(input())
n=int(input())
ans=0
if st=="mon":
    ans=n//6
elif st=="tue":
    ans=n//5
elif st=="wed":
    ans=n//4
elif st=="thu":
    ans=n//3 
elif st=="fri":
    ans=n//2
elif st=="sat":
    ans=n
elif st=="sun":
    ans=n//7
print(ans)