# Declaring variables
term = ''
power = ''
my_func = ''
derivative = ''

# Prompt user for a function
my_func = input("Enter a power function of the form ax^b. NOTE: a, b can't be 0: ")

# Find the numbers that represent the term
left_pointer = 0
while my_func[left_pointer] != "x":
    term += my_func[left_pointer]
    left_pointer += 1

# Find the numbers the represent the power
right_pointer = len(my_func) - 1
while my_func[right_pointer] != "^":
    power = my_func[right_pointer] + power
    right_pointer -= 1

# Typecasting
termf = float(term)
powerf = float(power)

# Calculating the derivative using the power rule
termf = powerf * termf
powerf -= 1
derivative = str(termf) + "x^" + str(powerf)

# Display derivative
print(f"Derivative of {my_func} is {derivative}")

