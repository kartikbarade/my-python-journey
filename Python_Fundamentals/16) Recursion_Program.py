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

2. Recursive Case: The recursive case is where the function calls itself with a smaller or simpler problem.

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

