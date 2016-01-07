# Python-loop
score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}

def scrabble_score(word):
    # make sure all letters are lower case:
    word = word.lower()
    # not asked for but  I found it useful to strip all whitespaces in a word;
    word = word.replace (" ", "")
    # set the total score = 0
    total = 0
    # start the for loop:
    for char in word:
        # total = total + score[char] works too.
        total += score[char]
    # return the score
    return total
