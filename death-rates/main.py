# Dataset Link
# https://catalog.data.gov/dataset/nchs-death-rates-and-life-expectancy-at-birth

# Importing necessary libraries
import json
import numpy as np
import pymongo
import math
import matplotlib.pyplot as plt

# Opening JSON file
with open('./death.json', 'r') as file:
    data = json.load(file)

# -------------------------------------------------
# TODO: Loading the file into a NoSQL Collection --
# -------------------------------------------------
# Establishing pymongo client
client = pymongo.MongoClient("localhost", 27017)

# Creating a population database
db = client["population"]

# Creating a people collection
people_col = db["people"]

# Initialize dictionary with appropriate key names
frame = {}
for i in range(0, len(data['meta']['view']['columns'])):
    key = data['meta']['view']['columns'][i]['fieldName']
    frame.setdefault(key, None)

# Creating records as a single dictionary and storing them in an apporpriate list
records_list = []
for i in range(0, len(data['data'])):
    record = dict(frame)
    for j in range(0, len(data['data'][i])):
       record[list(record.keys())[j]] = data['data'][i][j]
    records_list.append(record)

# Query to insert all records into the people collection
# people_col.insert_many(records_list)

# Verifying the collections exist
def viewCollections():
    for collections in db.list_collection_names():
        print("Collection: " + collections)
        print("----------")
# viewCollections()

print("Information about People Collection")
# Counting the number of documents in the collection
print("- Number of Documents: " + str(people_col.count_documents({})) + " records")
print("--------")

# ---------------------------------------
# TODO: Print data in an organized way --
# ---------------------------------------
print("Displaying the first 5 records")
r = people_col.find({}).limit(5)
for record in r:
    print("Record ID: " + record[":id"])
    print("Race: " + record["race"])
    print("Sex: " + record["sex"])
    print("Average Life Expectancy: " + record["average_life_expectancy"])
    print("Mortality: " + record["mortality"])
    print("\n")
print("--------")

# -------------------------------
# TODO: Descriptive Statistics --
# -------------------------------
# Descriptive statistics will be performed on average life expectancy
print("Descritive Statistics on Life Expenctancy")
r = people_col.find({})
avg_life_expectancy = []
for record in r:
    if not record["average_life_expectancy"] == None:
        avg_life_expectancy.append(float(record["average_life_expectancy"]))
life_expectancy_np_array = np.array(avg_life_expectancy)

# Average Life Expectancy
average = np.mean(life_expectancy_np_array)
print("Average: " + str(average))

# Median Life Expectancy
median = np.median(life_expectancy_np_array)
print("Median: " + str(median))

# Variance Life Expectancy
var = np.var(life_expectancy_np_array)
print("Variance: " + str(var))

# Standard Deviation Life Expectancy
std = np.std(life_expectancy_np_array)
print("Variance: " + str(std))

# -------------------------------
# TODO: Inferential Statistics --
# -------------------------------
# Research Question: I want to see how sex affects life expectency. So, we will run an independent samples t-test. I will use my alpha as 0.05.

# Populating male and female samples
male = []
female = []
r_female = people_col.find({"sex": "Female"})
r_male = people_col.find({"sex": "Male"})
for record in r_male:
    if not record["average_life_expectancy"] == None:
        male.append(float(record["average_life_expectancy"]))
for record in r_female:
    if not record["average_life_expectancy"] == None:
        female.append(float(record["average_life_expectancy"]))
male_np_array = np.array(male)
female_np_array = np.array(female)

# Finding standard deviation and average for each sample
# Male Average
male_average = np.mean(male_np_array)
# Male Standard Deviation
male_std = np.std(male_np_array)
# Female Average
female_average = np.mean(female_np_array)
# Female Standard Deviation
female_std = np.std(female_np_array)

# Stating Hypothesis: 
# - H0: Mean(male) = Mean(female)
# = H1: Mean(male) != Mean(female)

# Alpha = 0.05

# Degrees of Freedom
df = (len(male_np_array) - 1) + (len(female_np_array) - 1)
df_male = len(male_np_array) - 1
df_female = len(female_np_array) - 1

# Decision Rule
# Critical Value = 1.960
# if |t| > 1.960 then reject null

# Calculating Test-statistic
# Calculating sum of squares for each sample
ss_male = male_std*male_std * df_male
ss_female = female_std*female_std * df_female
# Calculating pooled variance
sp = (ss_male + ss_female) / (df_male + df_female) 
# Calculating t value
t = (male_average - female_average) / math.sqrt((sp/len(male_np_array)) + sp/len(female_np_array))

# State result
print("--------")
rejectNull = abs(t) > 1.96
print("Reject Null: " + str(rejectNull))

# ---------------------------------
# TODO: Plotting Relevant Graphs --
# ---------------------------------
# Plotting a logistic regression
r = people_col.find({"average_life_expectancy" : {"$nin": [None]}})
gender = []
for record in r: 
    if not record["sex"] == None:
        gender.append(record["sex"])
life_expectancy = avg_life_expectancy

plt.scatter(avg_life_expectancy,gender)
plt.xlabel('Gender', fontsize = 14)
plt.ylabel('Average Life Expectancy', fontsize = 14)
plt.show()