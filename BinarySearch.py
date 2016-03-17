# Python-loop
# A function to extract a player's last name
def format_name(name):
    return name.split(" ")[1] + ", " + name.split(" ")[0]

# The length of the dataset
length = len(nba)

# Implement the player_age function. For now, simply return what is specified in the instructions
def player_age(name):
    name = format_name(name)
    # Set the initial upper bound of the search
    # Set the initial lower bound of the search
    # Set the index of the first split (remember to use math.floor)
    # First guess at index (remember to format the guess)
    # Run search code until the name is equal to the guess, or upper bound is less than lower bound
        # If name comes before the guess
            # Change the appropriate bound
        # Else (name comes after the guess)
            # Change the appropriate bound
        # Set the index of our next guess (remember to use math.floor)
        # Retrieve and format our next guess
        
    ### Now that our loop has terminated, we must find out why ###
    # If the name is equal to the guess
        # Return the age of the player at index (column index 2 in dataset)
    # Else
        # Return -1, since our player was not found

def player_age(name):
    name = format_name(name)
    upper_bound = length - 1
    lower_bound = 0
    index = math.floor((upper_bound + lower_bound) / 2)
    guess = format_name(nba[index][0])
    while name != guess and upper_bound >= lower_bound:
        if name < guess:
            upper_bound = index - 1
        else:
            lower_bound = index + 1
        index = math.floor((lower_bound + lower_bound) / 2)
        guess = format_name(nba[index][0])
    if name == guess:
        return nba[index][2]
    else:
        return -1
    
curry_age = player_age("Stephen Curry")
griffin_age = player_age("Blake Griffin")
jordan_age = player_age("Michael Jordan")
