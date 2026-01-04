n=int(input())
arr=list(map(int,input().split()[:n]))
min_val=arr[0]
count=1
for i in range(1,n):
    if arr[i]>min_val:
        arr[i]=min_val
        count+=1 
print(count)