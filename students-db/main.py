import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password123",
  database="academy"
)

cursor = mydb.cursor()

# CREATING THE DATABASE
cursor.execute("CREATE DATABASE academy")

# CREATING THE STUDENTS TABLE
cursor.execute("CREATE TABLE students (full_name VARCHAR(255), age int,  program VARCHAR(255))")

# FLOODING THE STUDENTS TABLE
fill_query = "INSERT INTO students (full_name, age, program) VALUES (%s, %s, %s)"
records = [("Flint Tavern", 25, "Information Technology"), ("Ray Charles", 22, "Analytics"), ("Ponce Dart", 29, "Psychology")]
cursor.executemany(fill_query, records)
mydb.commit()

# VIEWING THE STUDENTS TABLE
cursor.execute("SELECT * FROM students")
result = cursor.fetchall()
for row in result:
    print(f"{row[0]}, {row[1]}, is in the {row[2]} program")

# CHANGING THE NAME OF A COLUMN TO THE STUDENTS TABLE
change_column_name_query = "ALTER TABLE students CHANGE program major VARCHAR(255)"
cursor.execute(change_column_name_query)
mydb.commit()

# VIEWING THE DESCRIPTION OF COLUMNS IN THE STUDENTS TABLE
cursor.execute("DESC students")
myresult = cursor.fetchall()
for i in myresult:
    print(i)

# -------- Module 9 Assignment --------

# ADDING MORE COLUMNS TO THE TABLE
alter_query1 = "ALTER TABLE students\
    ADD address VARCHAR(255)"
alter_query2 = "ALTER TABLE students\
    ADD school_id VARCHAR(255)"
cursor.execute(alter_query1)
cursor.execute(alter_query2)

# VIEWING THE DESCRIPTION OF COLUMNS IN THE STUDENTS TABLE
cursor.execute("DESC students")
myresult = cursor.fetchall()
for i in myresult:
    print(i)

# FLOODING NEW DATA IN THE TABLE
new_fill_query = "INSERT INTO students (full_name, age, major, address, school_id) VALUES (%s, %s, %s, %s, %s)"
records = [("Mark Boomer", 22, "Information Technology", "123 Seasme Street", "1345234"), ("John Drake", 25, "Analytics", "561 Bomp Street", "13425534"), ("Dart Palmer", 26, "Psychology", "876 Lukewarm Street", "9012342")]
cursor.executemany(new_fill_query, records)
mydb.commit()

# VIEWING THE TABLE AFTER FLOODING NEW DATA
cursor.execute("SELECT * FROM students")
result = cursor.fetchall()
for row in result:
    print(f"{row[0]}, {row[1]}, is in the {row[2]} program. Address: {row[3]}. Student ID: {row[4]}")

# CREATING THE COURSES TABLE
cursor.execute("CREATE TABLE courses (course_name VARCHAR(255), offered VARCHAR(255),  department VARCHAR(255))")

# FLOODING THE COURSES TABLE
courses_fill_query = "INSERT INTO courses (course_name, offered, department) VALUES (%s, %s, %s)"
course_records = [("Introduction to Political Science", "Summer 2023", "POLI"), ("Engineering Physics", "Fall 2023", "PHYS"), ("Group Theory", "Spring 2023", "MATH"), ("Topics in the Health Sciences", "Summer 2023", "HLTH")]
cursor.executemany(courses_fill_query, course_records)
mydb.commit()

# UPDATING A RECORD IN THE COURSES TABLE
course_update_query = "UPDATE courses SET course_name = \"Applied Health Sciences\" WHERE course_name = \"Topics in the Health Sciences\" "
cursor.execute(course_update_query)
mydb.commit()

# VIEWING THE COURSES TABLE
cursor.execute("SELECT * FROM courses")
result = cursor.fetchall()
for row in result:
    print(f"{row[0]}, is offered in {row[1]} by the {row[2]} department.")

# DELETING A COURSE FROM THE COURSES TABLE
course_delete_query = "DELETE FROM courses WHERE course_name = \"Introduction to Political Science\""
cursor.execute(course_delete_query)
mydb.commit()

# VIEWING THE COURSES TABLE AGAIN
cursor.execute("SELECT * FROM courses")
result = cursor.fetchall()
for row in result:
    print(f"{row[0]}, is offered in {row[1]} by the {row[2]} department.")

# COUNT NUMBER OF COURSES 
count_courses_query = "SELECT COUNT(*) AS number_of_courses FROM courses"
cursor.execute(count_courses_query)
result = cursor.fetchall()[0][0]
print("Number of Courses: " + str(result))

# AVERAGE AGE IN THE ACADEMY 
average_student_age_query = "SELECT AVG(age) FROM students"
cursor.execute(average_student_age_query)
result = cursor.fetchall()
print("Average Age in the Academy: " + str(result[0][0]))

# SUM OF AGE IN THE ACADEMY
sum_age_query = "SELECT SUM(age) FROM students"
cursor.execute(sum_age_query)
result = cursor.fetchall()
print("Sum of all Ages in the Academy: " + str(result[0][0]))