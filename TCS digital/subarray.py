arr=list(map(int,input().split()))
t=int(input())
for i in range(len(arr)):
    for j in range(i,len(arr)):
        if sum(arr[i:j+1])==t:
            print(i+1,j+1)
            exit()

print(-1)