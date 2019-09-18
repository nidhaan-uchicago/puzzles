def leap_year(year):
    '''
    on every year that is evenly divisible by 4
      except every year that is evenly divisible by 100
    unless the year is also evenly divisible by 400
    '''
    
    if year % 4 != 0:
        print("{} is not a leap year".format(year))
    else: 
        if year % 400 == 0:
            print("{} is a leap year".format(year))
        elif year % 100 == 0:
            print("{} is not a leap year".format(year))
        else:
            print("{} is a leap year".format(year))
