def score(word):
    # define point lists
    list_1 = ["a", "e", "i", "o", "u", "l", "n", "r", "s", "t"]
    list_2 = ["d", "g"]
    list_3 = ["b","c","m","p"]
    list_4 = ["f","h","v","w","y"]
    list_5 = ["k"]
    list_8 = ["j","x"]
    list_10 = ["q","z"]
    
    scores = [list_1, list_2, list_3, list_4, list_5, list_5, list_8, list_10]
    
    # convert word to lower case to simplify
    new_word = word.lower()

    # parse each word into a list of letters
    letter_list = list(new_word)
    
    # loop through each letter
    score = 0
    for letter in letter_list:
        for s in scores:
            if letter in s and (s == list_1):
                score = score + 1
            elif letter in s and (s == list_2):
                score = score + 2
            elif letter in s and (s == list_3):
                score = score + 3
            elif letter in s and (s == list_4):
                score = score + 4
            elif letter in s and (s == list_5):
                score = score + 5
            elif letter in s and (s == list_8):
                score = score + 8
            elif letter in s and (s == list_10):
                score = score + 10
    

    print(score)
        
        
