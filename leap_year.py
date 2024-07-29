'''Find next 20 leapyear'''

def isleapyr(yr):
    if yr%4==0:
        if yr%100==0:
            if yr%400==0:
                print("leap year")
            else:
                print("not leap year")
        else:
            print("leap year")
    else:
        print("not leap year")
yr=2021
print(isleapyr(yr))
