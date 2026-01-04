arr=list(map(int,input().split(",")))
new=0
for i in range(len(arr)):
    for j in range(i,len(arr)):
        new=max(new,sum(arr[i:j+1]))

print(new)

'''finding subarray and maximun sum of subarray'''