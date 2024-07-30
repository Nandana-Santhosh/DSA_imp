''' Reverse an array '''

arr=[1,4,6,8,3,5,2]
reversed_arr = arr[::-1]
print(reversed_arr)


def rl(arr,start,end):
    while start<end:
        arr[start],arr[end]=arr[end],arr[start]
        start+=1
        end-=1
arr=[3,5,7,8,91,3,5,7]
rl(arr,2,6)
print(arr)