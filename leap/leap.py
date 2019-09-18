def leap_year(year):
    if (year % 4) != 0:
        print("No")
    else:
       if (year % 100) == 0 & (year % 400) != 0:
            print("No")
       elif (year % 100) == 0 & (year % 400) == 0: 
            print("Yes")
        