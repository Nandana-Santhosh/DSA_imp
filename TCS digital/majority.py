
import math
n=int(input())
arr=list(map(int,input().split(" ")))[:n]
for i in arr:
    if arr.count(i)==math.floor(n/3):
        print(i)
        break