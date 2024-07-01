# One way ANOVA: One factor with two or more independent levels
# NOTE: For simplicity, this problem will only be limited three conditions and the number of participants in each condition will be limited to 7
num_of_levels = 3
level_count = 7

# Alpha value means that the null hypothesis is rejected 5% of the time when it is actually true.
alpha = 0.05 

# Here is our data 
condition1 = [9, 8, 7, 8, 8, 9, 8]
condition2 = [7, 6, 6, 7, 8, 7, 6]
condition3 = [4, 3, 2, 3, 4, 3, 2]
total_count = len(condition1) + len(condition2) + len(condition3)

# Calculating the degrees of freedom
df_between = num_of_levels - 1
df_within = total_count - num_of_levels
df_total = total_count - 1

# Finding the decision with the f-table (Found online)
# If th decision is greater than 3.556, reject H0
# NOTE: This is hard coded and will change based on the degrees of freedom within and between
decision_rule = 3.556

# Calculating sum of squares
def sum_of_squares_between(condition1, condition2, condition3):
    ss_between = ((sum(condition1)**2 + sum(condition2)**2 + sum(condition3)**2)/level_count) - ((sum(condition1) + sum(condition2) + sum(condition3))**2)/total_count
    return ss_between
ss_between = sum_of_squares_between(condition1, condition2, condition3)

def sum_of_squares_within(condition1, condition2, condition3):
    tmp = condition1 + condition2 + condition3
    accumulator = 0
    for i in tmp:
        accumulator += i**2
    ss_within = accumulator - ((sum(condition1)**2 + sum(condition2)**2 + sum(condition3)**2)/level_count)
    return ss_within
ss_within = sum_of_squares_within(condition1, condition2, condition3)

def sum_of_squares_total(condition1, condition2, condition3):
    tmp = condition1 + condition2 + condition3
    accumulator = 0
    for i in tmp:
        accumulator += i**2
    ss_total = accumulator - ((sum(condition1) + sum(condition2) + sum(condition3))**2)/total_count
    return ss_total
ss_total = sum_of_squares_total(condition1, condition2,  condition3)

# Calculating means square
def means_square_between():
    return ss_between / df_between
ms_between = means_square_between()

def means_square_within():
    return ss_within / df_within
ms_within = means_square_within()

# Calculating the f_statistic
f_statistic = ms_between / ms_within

if f_statistic > decision_rule:
    print("H0 is rejected")
else:
    print("H0 is accepted")

