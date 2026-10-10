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
A stack follows LIFO ---> Last in First Out

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
> when we call : count(3) a python creates a stack frame:
                --------------
                |   count(3) |
                --------------

> after the count(3) calls count(2)
               -------------
               | count(2)  |
               -------------
               | count(3)  | 
               -------------

> Then count(1)
                -------------
                | count(1)  |
                -------------
                | count(2)  |
                -------------
                | count(3)  | 
                -------------

and finally count(0)
                -------------
                | count(0)  |
                -------------
                | count(1)  |
                -------------
                  count(2)  |
                -------------
                | count(3)  | 
                -------------

> when count(0) reaches the base case, it returns.

> Now the stacks starts unwinding

count(0)-> removed
count(1)-> removed
count(2)-> removed
count(3)-> removed   
"""

#Find the sum of digits of a number
def sum_of_digit(n):
    if n == 0:
        return 0
    else:
        return (n%10) + sum_of_digit(n//10)
print(sum_of_digit(5432))

# Count the number of digits
def count_digit(n):
    if n<10:
        return 1
    else:
        return 1 + count_digit(n//10)
print(count_digit(24))

# Find the power of a number
def calculate_power(base,power):
    if power == 0:
        return 1
    if power < 0:
        return 1 / calculate_power(base,-power)
    else:
        return base * calculate_power(base, power-1)
print(calculate_power(2,5))

#--------------------------------------------------------------------------------------------

# Types of Recursion
""" a) Direct recursion 
When a function calls itself directly, it is called direct recursion.
"""
def fun(n):
    if n == 0:
        return
    print(n)
    fun(n-1)
fun(3)

""" b) Indirect recursion
When one function calls another function, which eventually calls the first function again, 
it is called indirect recursion (or mutual recursion).
"""
def fun1(n):
    if n<=0:
        return
    print("Function 1:",n)
    fun2(n-1)

def fun2(n):
    if n<=0:
        return
    print("Function 2:",n)
    fun1(n-1)
fun1(3)

""" c) tail recursion
When the recursive function call is the last operation performed by the function, 
it is called tail recursion.
"""
def count(n):
    if n == 0:
        return
    print(n)
    count(n-1) # last operation
count(3)

""" d) Head recusion
When a function calls itself first and performs its main 
operation after the recursive call returns, it is called head recursion.
"""
def count(n):
    if n == 0:
        return
    count(n - 1)
    print(n)  # After recursive call
count(3)
