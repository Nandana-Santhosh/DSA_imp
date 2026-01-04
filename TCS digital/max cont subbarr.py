arr=list(map(int,input().split(",")))
res=[]
k=int(input())
for i in range(len(arr)-k+1):
    res.append(max(arr[i:i+k]))
print(res)

'''how to access sub array with certain windowsize'''
