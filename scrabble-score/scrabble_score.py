def score(word):
    letter_list= list(word)
    score= 0
    for letter in letter_list: 
        if letter== "a" or letter== "e" or letter== "i" or letter== "o" or letter== "u" or letter== "l" or letter== "n" or letter== "r" or letter== "s" or letter== "t":
            score= score + 1
        elif letter== "d" or letter== "g":
            score == score + 2
        elif letter== "b" or letter== "c" or letter== "p" or letter== "m":
            score = score + 3
        elif letter== "f" or letter== "h" or letter== "v" or letter== "w" or letter== "y":
            score= score + 4
        elif letter== "k":
            score= score + 5
        elif letter== "j" or letter== "x":
            score= score + 8
        else:
            score= score + 10
            
    print(score)
            
        
        


