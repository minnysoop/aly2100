# Trying to answer the question: What is the impact of schooling on the lifespan of humans?

# Import necessary modules
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Reading the data
life_expectancy = pd.read_csv('data.csv')

# Replace spaces in column names with "_"
life_expectancy.columns = [c.replace(' ', '_') for c in life_expectancy.columns]

# Extracting necessary columns
schooling = life_expectancy["Schooling"]
lifespan = life_expectancy["life_expectancy"]

# Sorting school data
# schooling = schooling.sort_index(ascending=True)

# Plotting two data sets
plt.plot(schooling, lifespan, 'ro', markersize=2, color='darkblue')
plt.xlabel("Schooling (Years)")
plt.ylabel("Life Expectancy (Years)")
plt.title('Impact of Schooling on Life Expectancy')
# plt.show()

# Creating a linear regression model
# 1. Size of the used data of interest: Schooling
size = np.size(schooling)

# 2. Average of both sets
iv_avg = np.mean(schooling)
dv_avg = np.mean(lifespan)

# 3. Calculating deviations about the x
SSxy = np.sum(lifespan*schooling) - size*dv_avg*iv_avg
SSxx = np.sum(schooling*schooling) - size*iv_avg*iv_avg

# 4. Calculating coefficients for the linear equation
b_1 = SSxy / SSxx
b_0 = dv_avg - b_1*iv_avg

# Plotting the regression model
linear_equation = b_0 + b_1*schooling
plt.plot(schooling, linear_equation, color = "g")
plt.show()

