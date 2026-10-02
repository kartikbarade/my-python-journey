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