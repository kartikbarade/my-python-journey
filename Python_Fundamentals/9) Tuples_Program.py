"""
-------------- Tuples --------------
A tuple in Python is an ordered and immutable collection of elements 
used to store multiple values in a single variable.
Tuples are similar to lists, but the main difference is that tuples cannot 
be changed after they are created.
A tuple is created using parentheses (), and its elements can be of different
data types such as integers, strings, floats, lists, or even other tuples.

"""

#  Creating tuple
# a) Using Parentheses ()
numbers = (1,2,3,4,5)
print(numbers)

data = ("kartik", 21, "pune", 101, "ISBM")
print(data)

t = (10,)# For a single-element tuple,use a comma
print(type(t))

# b) Without Parentheses(packing)
# Python allows us to create a tuple without using parentheses. This is called tuple packing.
numbers = 1,2,3,4,5
print(numbers)

data = "kartik", 21, "pune", 101, "ISBM"
print(data)

a = 10 
b = 20 
c = 30

d = a,b,c
print(d)

# c) Empty Tuple
e_tuple = ()
print(e_tuple)
print(len(e_tuple))

