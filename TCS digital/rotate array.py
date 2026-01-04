arr = list(map(int, input().split()))  # Take input as space-separated numbers
rotated_arr = arr[-2:] + arr[:-2]  # Move last 2 elements to the front
print(crotated_arr)