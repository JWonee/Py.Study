#나
"""
year = int(input("Year = "))

if year%4 == 0:
    if year%100 == 0:
        if year%400 == 0:
            print("1")

        else:
            print("0")
    else:
        print("1")
else:
    print("0")
"""

#간단히

year = int(input("Year = "))

if (year%4 == 0 and year % 100 !=0) or year % 400 == 0:
    print(1)
else:
    print(0)
