import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import mysql.connector

# Reading the data
mental_health_df = pd.read_csv('mental_health.csv')

# ----- Descriptive Statistics -----
# Mean
mean = mental_health_df['Age'].mean()

# Median
median = mental_health_df['Age'].median()

# Mode
mode = mental_health_df['Choose your gender'].mode()[0]

# Standard Deviation
std_age = mental_health_df['Age'].std()

# Variance
var_age = mental_health_df['Age'].var()

# Displaying Output
print("Descriptive Statistics for Mental Health Data Set")
print(f"Mean AGE: {mean}")
print(f"Median AGE: {median}")
print(f"Mode GENDER: {mode}")
print(f"Standard Deviation of AGE: {std_age}")
print(f"Variance of AGE: {var_age}")

# Loading data...
student_mental_health_db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password123",
  database="mental_health_research"
)

# Creating cursor
cursor = student_mental_health_db.cursor()

# Creating the database
# cursor.execute("CREATE DATABASE mental_health_research")

# Creating the table
# cursor.execute("CREATE TABLE student_survey_data (timestamp VARCHAR(255), gender VARCHAR(255), age VARCHAR(255), course VARCHAR(255), current_year VARCHAR(255), cgpa VARCHAR(255), maritalStatus VARCHAR(255), depression VARCHAR(255), anxiety VARCHAR(255), panic_attack VARCHAR(255), seeking_treatment VARCHAR(255))")

# Extracting data from csv to list of tuples
def extractCSV(dataframe):
    records = []
    for i in range(1, len(mental_health_df.index)):
        tmp = []
        record = dataframe.iloc[i]
        for data in record:
            if data == None or data == "":
                tmp.append("N/A")
            tmp.append(str(data))
        records.append(tuple(tmp))
    return records

# Flooding table with data
fill_data = extractCSV(mental_health_df)
fill_query = "INSERT INTO student_survey_data (timestamp, gender, age, course, current_year, cgpa, maritalStatus, depression, anxiety, panic_attack, seeking_treatment) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
# cursor.executemany(fill_query, fill_data)
# student_mental_health_db.commit()

# Viewing the table after flooding
cursor.execute("SELECT * FROM student_survey_data")
result = cursor.fetchall()
for row in result:
    print(f"(Timestamp: {row[0]}, Gender: {row[1]}, Age: {row[2]}, Course: {row[3]}, Current Year: {row[4]}, CGPA: {row[5]}, Marital Status: {row[6]}, Depression: {row[7]}, Anxiety: {row[8]}, Panic Attacks: {row[9]}, Seeking Treatment: {row[10]})\n")

# Finding Standard Error of the Mean for Age
std_err_age = np.std(mental_health_df['Age'], ddof=1) / np.sqrt(len(mental_health_df.index))
print("Standard Error for Age: " + str(std_err_age))

# Plotting a Distribution Curve 
# NOTE: Becuase I had a lot of categorical data, I plotted a barchart 
depression = mental_health_df[['Do you have Depression?', 'Age']]
mental_health_df.groupby('Age').size().plot(kind='bar')
plt.show()
mental_health_df.groupby('Do you have Depression?').size().plot(kind='bar')
plt.show()
