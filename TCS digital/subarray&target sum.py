arr=list(map(int,input().split(",")))
t=int(input())
for i in range(len(arr)):
    for j in range(i,len(arr)):
        if(sum(arr[i:j+1])==t):
            print(arr[i:j+1])
'''
output::
3,4,-7,1,3,3,1,4
7
[3, 4]
[3, 4, -7, 1, 3, 3]
[1, 3, 3]
[3, 3, 1]
'''