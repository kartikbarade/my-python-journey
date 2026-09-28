"""
                              Functions
A function is a reusable block of code that performs a specific task.
Instead of writing the same code again and again, we can define a function 
once and call it whenever required.
"""
# Example
def hello():
    print("Hello, Welcome to Python!")

hello()

"""
def - keyword used to define a function
greet - function name
() - parentheses for parameters
hello() - function calling
"""
#----------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------
# Types of Functions
# a) Built in Functions
""" Functions are already provided by python such as print(), len(), type(), input(), int(),
str(), max(), min(), sum() etc.
"""
name = "Kartik"
print(name)      # print()
print(len(name)) # len()
print(type(name))# type()

stu_name = input("Enter student name : ") # input()
print(stu_name)

number = [10,20,30]  
result = sum(number) # sum()
print(result)

number = [10,20,30]
result = min(number) # min()
print(result)

number = [10,20,30]
result = max(number) # max()
print(result)

#------------------------------------------------
# b) User defined functions 
""" A function created by the programmer is called a user defined function.
"""
def add():
    a = 10
    b = 20
    c =a + b
    print(c)
add()

# function with parameter
def add(a,b):
    c = a + b
    print(c)
add(100,200)

# Examples:--------
# average of 3 numbers
def average():
    a = 10
    b = 20
    c = 30

    sum = a+b+c
    avg = sum/3
    print(avg)
average()

# addition of two number user define value
def calc_add():
    num1 = int(input("enter a 1st number :"))
    num2 = int(input("enter a 2nd number :"))
    result = (num1 + num2)
    print(result)
calc_add()

#------------------------------------------------
# c) function with return value
""" A function can return a result using the return statments
"""
def add(a,b):
    return a + b
c = add(1,2)
print(c)

#------------------------------------------------
# d) lambda function 
"""A lambda function is a small anonymous function.
"""
# normal function
def square():
    x = 5
    squ = x*x
    print(squ)
square()

# using lambda
square = lambda x:x*x
print(square(5))

add = lambda a,b: a+b
print(add(1000,2000))

sub = lambda a,b: a-b
print(sub(20,10))