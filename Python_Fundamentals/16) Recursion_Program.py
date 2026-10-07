"""
Recursion is a programming technique where a function calls itself in order to solve a problem. 
It is often used to solve problems that can be broken down into smaller, similar subproblems.
"""
# example
def count(n):
    if n == 0:
        return
    print(n)
    count(n-1)
count(5)

"""Components of Recursion---
A recursive function generally has two important components:
1. Base Case: The base case tells the function when to stop calling itself.

2. Recursive Case: The recursive case is where the function calls itself 
with a smaller or simpler problem.

Syntax---->
def recursive_function(parameters):
    if base_case_condition:
        return base_result
    else:
        return recursive_function(modified_parameters)
"""

# Calculate factorial of a number using recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))

# Print numbers from 1 to 5
def num(n):
    if n > 5:
        return 
    print(n)
    num(n+1)
num(1)

# Print Even number
def even(n):
    if n == 0:
        return 
    
    even(n-1)
    if n %2 ==0:
        print(n)
        
even(20)

# Print Odd number
def odd(n):
    if n == 0:
        return
    odd(n-1)
    if n % 2 != 0:
        print(n)
odd(20)

print("-------------------------------------------------------------")
# Sum of n natural number
# using for loop
num = 5
sum =0
for i in range(1,num+1):
    sum = sum + i
print("Using for loop",sum)

# using recursion
def sum(n):
    if n == 0:  # base case
        return 0
    else:
        return n + sum(n-1)   # recursive case
print("Using recursion",sum(5))

#-----------------------------------------------------------------------------------------------
"""    Call Stack of Recursion in Python
When a function is called,Python puts that function's information into a stack. 
When the function finishes,it is removed from the stack.

"""
# example 
def count(n):
    if n == 0:
        return
    print(n)
    count(n - 1)
count(3)
""" 
    -----How the Call Stack Works-----
    


"""


