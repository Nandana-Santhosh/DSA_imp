n=int(input())
#arr=list(map(int,input().split()))[:n] ## taking array as 1 2 3 4 5
#arr=list(map(int,input().split(",")))[:n]  ## taking array as 1,2,3,4,5
arr=[int(input())for _ in range(n)] ## taking input array as [1,2,3,4,5]
for i in range(n):
    if arr[i]==0:
        arr.remove(0)
        arr.append(0)
print(" ".join(map(str,arr))) # output as 1 2 3 4 5