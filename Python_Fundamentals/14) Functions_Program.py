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

#------------------------------------------------
# d) map function 
# Applies a given function to all items in a collection
# Syntax - map(function,iterable)
    # Ex 1
def c_to_f(temp):
    return (temp *9/5) + 32
      
celsics_temps = [23.1,30.1,32.3,31.1,40.4,45.7]
fahrenheit_temps = list(map(c_to_f,celsics_temps))
print(fahrenheit_temps)

     # Ex 2
def double(val):
    return val * 2
value = [2,3,4,5]
result = list(map(double,value))
print(result)


#----------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------
# Function Parameters and Arguments
""" When we create a function, we often need to pass data into it.
This is done using parameters and arguments. 

Parameter ---> A parameter is a variable written inside the function definition.
def add(a, b):
    print(a + b)

    # here a and b is the parameter

Argument ---> An argument is the actual value passed when calling the function.
add(10, 20)

# Here 10 and 20 are arguments.
"""
# example --
def add(a,b):
    c = a + b
    print(c)
add(10,20)
#-------------------------------#
def student(name,age):
    print("Name: ", name)
    print("Age: ", age)
student("kartik",21)


# Types of Arguments 
# a) Positional Arguments
""" In positional arguments, Values are passed according to their position/order. """
def student(name,age):
    print("Name: ", name)
    print("Age: ", age)
student("Kartik", 21)   # The order is important

# b) Keyword Arguments
""" In keyword arguments, we specify the parameter name while passing the value. """
def student(name, age):
    print("Name :", name)
    print("Age :", age)
student(age = 21, name= "Kartik")  # the order doesn't matter

# c) Default Arguments
""" A default arguments has a dafault value. If the user dosen't provide that arguments,
Python used a default values. """
def student(name="Kartik"):
    print("Hello ", name)
student()

def student(name, age=21, city="Pune"):
    print("Name :", name)
    print("Age :", age)
    print("City :" , city)

student("Kartik")

# d) Variable - length Arguments 
"""Sometimes we don't know how many arguments the user will pass.
    i) *args   ii) **kwargs
"""
# i) *args
def numbers(*args):
    print(args)
numbers(10,20,30,40,50)

def add(*numbers):
    total =0
    for i in numbers:
        total = total + i
    print("Total :", total)
add(10,20,30)

# ii) **kwargs
def student(**kwargs):
    print(kwargs)
student(name = 'kartik', age=21, city="Pune")

def student(**details):
    print("Name:", details["name"])
    print("Age:", details["age"])
    print("City:", details["city"])
student(name="Kartik", age=21, city="Pune")


#-----------------------------------------------------------------------------------
# Argumnents passing mechanism
"""In Python, it is more accurate to say that Python uses "pass-by-object-reference".
"""
def change(x):
    x = 100
    print(x)
num =50
change(num)
print(num)

def change(numbers):
    numbers.append(100)

list = [10,20,30,40]
change(list)
print(list)