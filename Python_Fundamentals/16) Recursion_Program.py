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