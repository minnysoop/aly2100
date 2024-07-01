#####################
##### Problem 1 #####
#####################
# Given a seven-digit number, generate every possible seven-letter word combination corresponding to that number

# Standard Keypad Mappings
# 2 АBC
# 3 DEF
# 4 GHI
# 5 JKL
# 6 MNO
# 7 PRS
# 8 TUV
# 9 WXY

# Other notes
# Possible cominations: 3^7 = 2187

# Assumptions
# A valid seven-digit will not contain 0's or 1's 

# Global Variables
keymap = {
    "2": ['A', 'B', 'C'], 
    "3": ['D', 'E', 'F'],
    "4": ['G', 'H','I'],
    "5": ['J', 'K', 'L'],
    "6": ['M', 'N', 'O'],
    "7": ['P', 'R', 'S'],
    "8": ['T', 'U', 'V'],
    "9": ['W', 'X', 'Y']
           }

lettermap = {
    "A": '2', 
    "B": '2',
    "C": '2',
    "D": '3',
    "E": '3',
    "F": '3',
    "G": '4',
    "H": '4',
    "I": '4',
    "J": '5',
    "K": '5',
    "L": '5',
    "M": '6',
    "N": '6',
    "O": '6',
    "P": '7',
    "R": '7',
    "S": '7',
    "T": "8",
    "U": "8",
    "V": "8",
    "W": "9",
    "X": "9",
    "Y": "9"
    }

# Entry point of the program
def main():
    # Prompt user for seven-digit number
    print("Input Format: ###-####")
    seven_digit_number = input("Enter a seven digit number: ").replace("-", "")
    # Prompt user again if seven-digit number isn't valid
    while not isValid(seven_digit_number):
        print("Input Format: ###-####")
        seven_digit_number = input("Enter a seven digit number: ").replace("-", "")
    # Generate combinations and print them
    word_list = combinations(seven_digit_number)
    for i in range(0, len(word_list)):
        print(str(i + 1) + ") " + word_list[i])

# Returns true if the given seven-digit number is valid
def isValid(number):
    if len(number) != 7:
        return False
    for digit in number:
        if digit == "1" or digit == "0":
            return False
    return True

# Generate combinations with lists
def combinations(number):
    word_list = []
    for i in range(0, 3):
        for j in range(0, 3):
            for k in range(0, 3):
                for l in range(0, 3):
                    for m in range(0, 3):
                        for n in range(0, 3):
                            for o in range(0, 3):
                                buffer = keymap[number[0]][i] + keymap[number[1]][j] + keymap[number[2]][k] + keymap[number[3]][l] + keymap[number[4]][m] + keymap[number[5]][n] + keymap[number[6]][o]
                                word_list.append(buffer)
    return word_list

# Running the program for the first problem
# main()

#####################
##### Problem 2 #####
#####################

# Given a valid seven letter word, find the corresponding numbers to it
def possible_numbers(word):
    number = ""
    for letter in word:
        number += lettermap[letter]
    number = number[0:3] + "-" + number[3:]
    return number

# Tests
print(possible_numbers("BIGDATA") == "244-3282")
print(possible_numbers("PETCARE") == "738-2273")
print(possible_numbers("NUMBERS") == "686-2377")

