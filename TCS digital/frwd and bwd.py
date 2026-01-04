def fb(s):
    if len(s)<=1:
        print(1)
    bck=s[1:]+s[0]
    fwd=s[-1]+s[:-1]
    if bck==fwd:
        print(1)
    else:
        print(0)
s=str(input())
fb(s)
