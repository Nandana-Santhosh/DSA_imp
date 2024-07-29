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



'''def is_leap_year(year):
    # Check if a year is a leap year
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

def find_next_leap_years(start_year, count):
    leap_years = []
    year = start_year
    
    while len(leap_years) < count:
        if is_leap_year(year):
            leap_years.append(year)
        year += 1
        
    return leap_years

# Starting year
start_year = 2024  # You can set this to the current year or any other starting point

# Find the next 20 leap years
next_20_leap_years = find_next_leap_years(start_year, 20)

# Print the next 20 leap years
print("The next 20 leap years are:")
for year in next_20_leap_years:
    print(year)
'''


