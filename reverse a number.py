'''Python Program to Reverse a Number'''
def reversenum(num):
    reverse=0
    for _ in str (num):
        reminder=num%10
        reverse=reverse*10+reminder
        num=num//10
    return reverse
print(reversenum(12345))

#lst method
def revrselist(num):
    numlist=list(str(num))
    reverse=''.join(numlist[::-1])
    return reverse
print(revrselist(12345))