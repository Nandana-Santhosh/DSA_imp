'''program to print the prime numbers from 100 to 1000'''

a=100
b=1000
for i in range(a,b+1):
    if i==1:
        continue
    flag=1
    for j in range(2, i//2 +1):
        if (i%j==0): #divisible not prime
            flag=0
            break
    if flag==1:
        print(i,end=" ")