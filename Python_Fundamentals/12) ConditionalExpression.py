"""
Conditional statements in Python are used to make decisions in a program.
They allow Python to execute different blocks of code depending on whether a 
condition is True or False.

or example, if a student scores 40 or more marks, the student passes.
Otherwise, the student fails.
Python provides different ways to implement conditions:
    a)if Statement
    b)if-else Statement
    c)if-elif-else Statement
    d)Conditional Expression (Ternary Operator
"""
# a) if Statement
age = int(input("Enter the age :-"))
if age >18:
    print("Candidate are elegible")

#-----------------------------------------------------------
""" Write a Python program to take a number from the user and check whether the 
number is positive. If the number is positive, print "Positive Number"."""

num = int(input("Enter the Number :-"))
if num > 0:
    print(f'The {num} is positive number')

#-----------------------------------------------------------  
"""Write a Python program to take a student's marks. If the marks are greater than 
or equal to 40, print "Student Passed"."""
marks = int(input("Enter the students marks :- "))
if marks >=40:
    print("Student Passed")

#-----------------------------------------------------------  
"""Write a Python program to take a password from the user. If the password is "python123",
 print "Login Successful"."""
password = input("Enter the password : ")
if password == 'python123':
    print("Login Successful")

#-----------------------------------------------------------
"""Write a Python program to take two numbers from the user. If the first number is greater than 
the second number, print "First number is greater"."""
num1 = int(input("Enter the 1st number : "))
num2 = int(input("Enter the 2nd number : "))
if num1>num2:
    print("First number is greater")

#-----------------------------------------------------------
"""Write a Python program to take a number. If the number is divisible by 5, print "Number is 
divisible by 5"."""
num = int(input("Enter the number :"))
if num % 5 == 0:
    print("Number is divisible by 5")

#-----------------------------------------------------------
"""Write a Python program to take a character from the user. If the character is "a", print 
"You entered a"."""
char = input("Enter a charater : ")
if char == 'a':
    print("You entered a")


#----------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------
# b) if-else statement
num = int(input("Enter the number :- "))
if num % 2 == 0:
    print("Number is Even")
else:
    print("Number is Odd")
    
#-----------------------------------------------------------
"""Write a Python program to check whether a number is positive or negative."""
num = int(input("Enter the number :"))
if num >= 0:
    print(f"The {num} is a positive number")
else:
    print(f"The {num} is a negative number")

#-----------------------------------------------------------
"""Take a person's age as input. If the age is 18 or above, print "Eligible to Vote". 
Otherwise, print "Not Eligible"."""
age = int(input("Enter your age"))
if age >=18:
    print("Eligible to Vote")
else:
    print("Not Eligible")

#-----------------------------------------------------------
"""Take student marks as input. If marks are greater than or equal to 35, print "Pass".
 Otherwise, print "Fail"."""
marks = int(input("Enter your marks"))
if marks >= 35:
    print("Pass")
else:
    print("Fail")

#-----------------------------------------------------------
"""Take two numbers from the user. Check which number is greater."""
a = int(input("Enter the 1st num"))
b = int(input("Enter the 2nd num"))
if a<=b:
    print(f"The {a} is greater")
else:
    print(f"The {b} is greater")

#-----------------------------------------------------------
# if-elif-else
marks = int(input("Enter the marks : "))
if marks >= 90:
    print("Grade A")
elif marks >=75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Fail")

#-----------------------------------------------------------
"""Student Grade
Take student marks as input and display the grade:
90–100: Grade A
75–89: Grade B
60–74: Grade C
40–59: Grade D 
Below 40: Fail"""
marks = int(input("Enter the marks : "))
if marks >=90 and marks <=100 :
    print("Grade A")
elif marks >=75   :
    print("Grade B")
elif marks >=60:
    print("Grade C")
elif marks >=40 :
    print("Grade D")
else:
    print("Fail")

#-----------------------------------------------------------
"""Take three numbers from the user and print the largest number using if-elif-else."""
a = int(input("Enter the 1st number"))
b = int(input("Enter the 2nd number"))
c = int(input("Enter the 3rd number"))

if a >=b and a>=c:
    print("A is largest number")
elif b>=a and b>=c:
    print("B is largest number")
else:
    print("C is largest number")

#-----------------------------------------------------------
"""Check Temperature
Take temperature as input:
Above 35: Very Hot
25–35: Warm
15–24: Cool
Below 15: Cold"""
temperature = int(input("Enter the temperature"))
if temperature >= 35:
    print("Very Hot")
elif temperature >= 25:
    print("Warm")
elif temperature >= 15:
    print("Cool")
else:
    print("Cold")

#-----------------------------------------------------------
"""Take two numbers and an operator (+, -, *, /). Perform the 
selected operation using if-elif-else."""
num1 = int(input("Enter the 1st number : "))
num2 = int(input("Enter the 2nd number : "))
operator = input("Enter operator (+, -, *, /): ") 

if operator =='+':
    print("Result = ", num1 + num2)
elif operator == '-':
    print("Result = ", num1 - num2)
elif operator == '*':
    print("Result = ", num1 * num2)
elif operator == '/':
    print("Result = ", num1 / num2)
else:
    print("Invalid Choice")


