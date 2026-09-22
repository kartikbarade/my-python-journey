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



# b) if-else statement
num = int(input("Enter the number :- "))
if num % 2 == 0:
    print("Number is Even")
else:
    print("Number is Odd")

