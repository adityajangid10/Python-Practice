# ==========================================
# Python Variables Practice
# Author: Aditya Jangid
# Topic: Variables in Python
# ==========================================
# A variable is used to store data in memory.
# Storing personal information

name = "Aditya Jangid"
age = 21
city = "Jaipur"
college = "BCA"

print("----- Personal Information -----")
print("Name :", name)
print("Age :", age)
print("City :", city)
print("Course :", college)

print()

# Updating variable value

print("----- Updating Variables -----")

age = age + 1

print("Age after one year:", age)

print()

# Multiple variable assignment

print("----- Multiple Assignment -----")

bike_name, model, year = "Hero Xtreme 160R", "Stealth Edition", 2024

print("Bike Name:", bike_name)
print("Model:", model)
print("Year:", year)

print()

# Variables with different data types

print("----- Different Data Types -----")

student_name = "Aditya"
student_age = 21
student_percentage = 85.5
is_placed = False

print("Name:", student_name)
print("Age:", student_age)
print("Percentage:", student_percentage)
print("Placed:", is_placed)

print()

# Checking variable types

print("----- Variable Types -----")

print(type(student_name))
print(type(student_age))
print(type(student_percentage))
print(type(is_placed))

print()

# Performing calculations using variables

print("----- Variable Calculations -----")

python_marks = 92
sql_marks = 88
ml_marks = 90

total_marks = python_marks + sql_marks + ml_marks
average_marks = total_marks / 3

print("Total Marks:", total_marks)
print("Average Marks:", average_marks)

print()

# Swapping variable values

print("----- Swapping Variables -----")

x = 10
y = 20

print("Before Swap")
print("x =", x)
print("y =", y)

x, y = y, x

print("After Swap")
print("x =", x)
print("y =", y)

print()

# Creating variables for future AI journey

print("----- Future Goals -----")

goal = "Machine Learning Engineer"
target_projects = 15
daily_study_hours = 7

print("Career Goal:", goal)
print("Target Projects:", target_projects)
print("Daily Study Hours:", daily_study_hours)

print()

print("Variables practice completed successfully!")
