# Importing Necessary Modules
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import statsmodels.api as sm

# Reading the necessary csv file
records_df = pd.read_csv('heart_failure_clinical_records_dataset.csv')

# Statistics on platelets
# NOTE: platelets: platelets in the blood (kiloplatelets/mL)
platelets_df = records_df['platelets']

# Mean
mean_platelets = platelets_df.mean()
# Median
median_platelets = platelets_df.median()
# Mode
mode_platelets = platelets_df.mode()
# Standard Deviation
std_platelets = platelets_df.std()
# Variance
var_platelets = platelets_df.var()
print("Statistics on Platelets")
print(f"Mean: {mean_platelets} kiloplatelets/mL\nMedian: {median_platelets} kiloplatelets/mL\nMode: {mode_platelets[0]} kiloplatelets/mL\nStandard Deviation: {std_platelets} kiloplatelets/mL\nVariance: {var_platelets} kiloplatelets/mL")
print("---------")

# Building a Logisitic Regresion Model for Creatinine Phosphokinase and Death Events

# Independent Variable 
# NOTE: Creatinine Phosphokinase is the number of CPK enzymes (Proteins that help break down molecules) in the blood
x1 = records_df['creatinine_phosphokinase']
# Dependent Variable
y = records_df['DEATH_EVENT']

# In the package I was using, the logistic regression did not have a constant by default. This means our model would never have an instance of 0. Which, in our case, is needed because it's possible for someone to have 0 levels of ejection fraction.
x1 = sm.add_constant(x1)

# Creates a logistic regression model instance
logistic_regression = sm.Logit(y, x1)

# Fits the logistic regression to our data
log_fit_results = logistic_regression.fit()

# Matching the Sigmoid function with our data variables. This wil serve as our skeleton to create our logistic regression graph to fit onto our figure
def f(x, b0, b1):
    return np.array(np.exp(b0 + x * b1) / (1 + np.exp(b0 + x * b1)))

# Here we have to sort our data points based on the parameters of our logistic regression
f_sorted = np.sort(f(x1,log_fit_results.params[0],log_fit_results.params[1]))
x_sorted = np.sort(np.array(x1))

# Plotting the regression line
plt.scatter(records_df['creatinine_phosphokinase'],records_df['DEATH_EVENT'])
plt.plot(x_sorted,f_sorted)
plt.xlabel('Creatinine Phosphokinase (mcg/L)', fontsize = 14)
plt.ylabel('Death', fontsize = 14)
plt.title("Logistic Regression Model")
# plt.show()

# Conducting a one sample t test 
# NOTE: The problem is formulated in the given report, only the calculations are on here

# Average Platelet Count for Heart Failure Patients
avg_platelets = mean_platelets

# How many patients are anaemic 
def countAnaemic():
    count = 0
    anaemic_rows = []
    for i in range(0, 299):
        if records_df['anaemia'][i] == 1:
            anaemic_rows.append(records_df['platelets'][i])
            count += 1
    return anaemic_rows
anaemic_platelets_rows = np.array(countAnaemic())

# Getting the average of sample
mean_sample = np.mean(anaemic_platelets_rows)

# Getting the standard deviation of sample
std_sample = np.std(anaemic_platelets_rows, ddof=1)

# Calculating Degrees of Freedom
degreesOfFreedom = 129 - 1

# Decision rule 
decisionRule = 1.980

# Calculate Test Statistics
t = (mean_sample - avg_platelets)/(std_sample)/129

# Our Result
print(f"REJECT NULL?: {abs(t) > decisionRule}")