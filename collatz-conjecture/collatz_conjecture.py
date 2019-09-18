def steps(number):
    if number > 0:
    #assert number > 0, "ERROR"
        i = 0
        while (number != 1):
            if (number % 2) == 0:
                # divide number by 2, store as new number
                number = number/2
                i = i + 1
            else:
                # do 3x + 1, store as new number
                number = 3*number + 1
                i = i + 1
    else:
        raise ValueError("number cannnot be negative")

    return i
    
    
