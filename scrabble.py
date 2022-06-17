import wordscore

with open("sowpods.txt","r") as infile:
    raw_input = infile.readlines()
    data = [datum.strip('\n') for datum in raw_input]

def run_scrabble(rack):
    
    """
    rack: combination of two to seven letters
    
    Returns:
        1) The total list of valid words sorted by score and word
        2) The total number of valid words as an integer
    """
    
    if type(rack) != str:
        print("Please input a string")
        return
    
    if len(rack) > 7 or len(rack) < 2:
        print("Please input a rack that has two to seven letters")
        return
         
    rack = rack.lower() # Converts all the letters into lower case
    rack_dict = {} # Creates a dictionary for the rack
    
    for letter in rack:
        if letter in rack_dict:
            rack_dict[letter] += 1
        else:
            rack_dict[letter] = 1
        
    if "*" in rack:
        if rack_dict["*"] == 2:
            print("You cannot use more than two wildcards")
            return
        
    if "?" in rack:
        if rack_dict["?"] == 2:
            print("You cannot use more than two wildcards")
            return
            
    valid_words = [] # Creates a list of tuple that contains valid Scrabble word that can be constructed by the rack, and its score
    length = 0 # The total number of valid words as an integer
    valid = False # Determines whether a word can be created from the rack

    for word in data:
        copy = rack_dict.copy() # Creates copy of rack dictionary to prevent mutation of the orignal dictionary
        penalty = 0 # Tracks the score lost by using wildcard
        
        # Skips the word if we do not have enough letters to construct it
        if len(word) > len(rack):
            continue
        
        for letter in word.lower():
            
            # Checks if letter of the word is in the rack
            if letter not in copy:
                # Checks for wildcard "?"
                if "?" in copy and copy["?"] > 0:
                    penalty += score_word(letter) 
                    copy["?"] -= 1
                    valid = True
                    continue
                # Checks for wildcard "*"
                elif "*" in copy and copy["*"] > 0:
                    penalty += score_word(letter) 
                    copy["*"] -= 1
                    valid = True
                    continue
                valid = False
                break
                
            # Checks if we have enough letter in the rack
            elif copy[letter] <= 0:
                valid = False
                break
                
            # Checks for repeated letter use
            else:
                copy[letter] -= 1
                valid = True

        if valid:
            length += 1
            word_score = score_word(word) - penalty # Calculates the final score of word
            valid_words.append((word_score, word))

    # Sorts the list by score and then by words alphabetically
    output = sorted(valid_words, key=lambda x: x[0], reverse=True) 

    return (output, length)