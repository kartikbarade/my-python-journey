# Module in Python
""" A module is a python file (.py) that contains code such as functions, classes, variables,
statements. 
We can create a module once and reuse its code in other programs by importing it.
"""
# simple example
# create a module file (calculator.py)

import calculator
print("Addition : ", calculator.add(10,20))
print("Subtraction : ", calculator.sub(20,10))


num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
print("Addition : ", calculator.add(num1,num2))
print("Subtraction : ", calculator.sub(num1,num2))

#-----------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------
# Types of Modules
# a) Built in Modules
""" 
A module that is already provided by python is called a built in module.
Python provides many built in modules such as math, random, os, sys, datetime, time, json,
re, urllib, socket, email, logging, csv, sqlite3 etc
"""

import math
print(math.sqrt(25)) # sqrt()
print(math.pow(2,3)) # pow()
print(math.ceil(2.3)) # ceil()
print(math.floor(2.3)) # floor()
print(math.factorial(5)) # factorial()

# importing a specific function from a module
from math import sqrt
print(sqrt(25)) 

# import multiple functions from a module
from math import sqrt, pow
print(sqrt(36))
print(pow(2,4))

# using * to import all functions from a module
from math import *
print(sqrt(49))
print(pow(3,3))
print(ceil(2.7))
print(floor(2.7))
print(factorial(6))

# usinf alias name for a module
import math as m
print(m.sqrt(64))

# b) User defined Modules
"""A user-defined module is a Python module created by the programmer.
"""
# example 
print("Addition : ", calculator.add(100,200))
print("Subtraction : ", calculator.sub(200,100))
print("Multiplication : ", calculator.mul(10,20))
print("Division : ", calculator.div(20,0))


#-----------------------------------------------------------------------------------------------
import student

print(student.name)
print(student.age)

student.display_student()

# Module with a Variable and Function
import employee
print(employee.company)
employee.display_employee("Kartik", 50000)

#-----------------------------------------------------------------------------------------------

# dir() Function
""" It is used to find out what names/attributes are available inside an object or module.
"""
import math
print(dir(math))
print("---------------------------------------------------------------------------------------")

import calculator
print(dir(calculator))
print("---------------------------------------------------------------------------------------")

import os
print(dir(os))

# dir() with a string
name = "Kartik"
print(dir(name))

# dir() with a list
numbers = [1, 2, 3, 4, 5]
print(dir(numbers))

#-----------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------
import student_result_module
student_result_module.student_result()

#-----------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------
# math module
import math
print(math.sqrt(25)) # sqrt()
print(math.pow(2,3)) # pow()
print(math.ceil(2.3)) # ceil()
print(math.floor(2.3)) # floor()
print(math.factorial(5)) # factorial()
print(math.gcd(12, 18)) # gcd()
print(math.lcm(12, 18)) # lcm()
print(math.pi) # pi

#------------------------------------------------------------
# Random module
# a) randint()
import random
print(random.randint(1,10))

for i in range(5):
    print(random.randint(1,100))


# b) choice()
import random
names = ["Kartik", "Yash", "Omkar","Ashwin","Rohit"]
print(random.choice(names))

# c) shuffle()
import random
numbers = [1,2,3,4,5]
print("Before shuffle : ", numbers)
random.shuffle(numbers)
print("After shuffle : ", numbers)

# d) random()
import random
for i in range(5):
    print(random.random()) # generates a random float number between 0 and 1

#------------------------------------------------------------
# datetime module
# a) date()
import datetime
today = datetime.date.today()
print("Today's date : ", today)

# b) time()
import datetime
current_time = datetime.datetime.now().time()
print("Current time : ", current_time)

# c) datetime()
import datetime
current_datetime = datetime.datetime.now()
print("Current date and time : ", current_datetime)

# d) difference between two dates
import datetime
date1 = datetime.date(2026, 10, 2)
date2 = datetime.date(2026, 10, 10)
difference = date2 - date1
print("Difference between two dates : ",difference)

#------------------------------------------------------------
# os module
# a) getcwd()
import os
current_directory = os.getcwd()
print("Current working directory : ", current_directory)

# b) listdir()
import os
current_directory = os.listdir()
print("Files and directories in current directory : ", current_directory)

# c) mkdir()
import os
new_directory = "NewFolder"

# d) checks whether a file or directory exists
import os
file_path = "example.txt"
if os.path.exists(file_path):
    print(f"{file_path} exists.")
else:
    print(f"{file_path} does not exist.")

#------------------------------------------------------------
# os module
# a) Python version
import sys
print("Python version : ", sys.version)

# b) sys.argv
import sys
print("Command-line arguments : ", sys.argv)

#------------------------------------------------------------
import sys
name = sys.argv[1]
print("Hello, ",name)

# c) sys.exit()
import sys
print("Program is started")
sys.exit()
print("Program is ended")