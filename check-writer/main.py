# Importing necessary libraries
import math

# INSTRUCTIONS
# Write a code that inputs a numeric check amount that is no more than 1000 and use the dictionary to write the word equivalent to the amount.

# APPROACH
# Creating a dictionary data structure in order to map the corresponding word equivalents

# IMPORTANT NOTE
# ASSUMPTIONS
# All provided numbers will be valid. Meaning, the string provided will yield a number less than ten thousand and will be a real number

# Creating a Check class
# Concept: For a class to be instantiated, a numeric value has to be specified. It's appropriate to say that every numeric value creates a Check object. 
class Check: 

    # Check constructor class
    def __init__(self, amount):
        self.amount = amount
        self.mapping = {
            1000: "THOUSAND",
            100: "HUNDRED",
            90: "NINETY",
            80: "EIGHTY",
            70: "SEVENTY",
            60: "SIXTY",
            50: "FIFTY",
            40: "FORTY",
            30: "THIRTY",
            20: "TWENTY",
            12: "TWELVE",
            11: "ELEVEN",
            10: "TEN",
            9: "NINE",
            8: "EIGHT",
            7: "SEVEN",
            6: "SIX",
            5: "FIVE",
            4: "FOUR",
            3: "THREE",
            2: "TWO",
            1: "ONE",
            0: "ZERO"
        }

    # Returns the integer part
    # FUNC --> INTEGER
    def split_integer(self):
        integer_part = ""
        for i in self.amount:
            if i == ".":
                break
            integer_part += i
        return integer_part 

    # Returns the fraction part 
    # FUNC --> INTEGER
    def split_fraction(self):
        fraction_part = ""
        point_found = False
        i = len(self.amount) - 1
        while i > 0:
            if self.amount[i] == ".":
                point_found = True
                break
            fraction_part = self.amount[i] + fraction_part
            i -= 1
        if not point_found:
            fraction_part = ""
        return fraction_part

    # Converts the integer part to words
    def convert_integer(self):
        integer_to_words = ""
        integer_part = self.split_integer()
        for i in range(0, len(integer_part)):
            # Only for the last two digits
            if i == len(integer_part) - 2:
                # CASE 1: Last two digits are 11 or 12
                if int(integer_part[i]) * 10 + int(integer_part[i + 1]) == 11 or int(integer_part[i]) * 10 + int(integer_part[i + 1]) == 12: 
                    final_digits = int(integer_part[i]) * 10 + int(integer_part[i + 1])
                    integer_to_words += self.mapping[final_digits] + " "
                    break
                # CASE 2: Last two digits are between 13 and 19 inclusive
                elif int(integer_part[i]) * 10 + int(integer_part[i + 1]) > 12 and int(integer_part[i]) * 10 + int(integer_part[i + 1]) < 20:
                    final_digits = int(integer_part[i]) * 10 + int(integer_part[i + 1])
                    if int(integer_part[i + 1]) == 3:
                        integer_to_words += "THIRTEEN "
                    elif int(integer_part[i + 1]) == 5:
                        integer_to_words += "FIFTHTEEN "
                    else:
                        integer_to_words += self.mapping[int(integer_part[i + 1])] + "TEEN "
                    break
                # CASE 3: Any other case
                else:
                    tens = int(integer_part[i]) * 10
                    ones = int(integer_part[i + 1])
                    integer_to_words += str(self.mapping[tens]) + " " + str(self.mapping[ones]) + " "
                    break
            if int(integer_part[i]) == 0:
                pass
            else:
                # For every other digit
                count = int(integer_part[i])
                place = math.pow(10, len(integer_part) - 1 - i)
                integer_to_words += str(self.mapping[count]) + " " + str(self.mapping[place]) + " "

        return integer_to_words

    # Converts the fraction part to words
    def convert_fraction(self):
        fraction_part = self.split_fraction()
        # We want to minimize the fraction to two decimal places but still allow the user to enter as many decimal places as they want
        if len(fraction_part) >= 3:
            fraction_part = str(int(round(float(fraction_part)/(math.pow(10, len(fraction_part))), 2) * 100))
        return "AND " + fraction_part + "/100"

    # Combines the output of the two functions above
    def into_words(self):
        word = self.convert_integer() + self.convert_fraction()
        return word.replace("ZERO ", "")

# TESTS
print(Check("9399.1582093").into_words())
print(Check("809.142093").into_words())
print(Check("8090.143").into_words())
print(Check("7001.143").into_words())


