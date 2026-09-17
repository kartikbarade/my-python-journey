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

#----------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------
"""
                                    Tuples vs List
Both lists and tuples are used to store multiple values in python. main difference is that list are 
mutable and tuples are immutable.
"""

# a) Mutability difference
list = [10,20,30,40]
list [2] = 50
print(list)         # Output --> [10, 20, 50, 40]

# tuple = (10,20,30,40)
# tuple [2] = 60  
# print(tuple)         # Output --> TypeError: 'tuple' object does not support item assignment

#----------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------
"""        Indexing and Slicing 

"""
# Indexing 
# positive indexing
numbers = (10,20,30,40,50)
print(numbers[0])
print(numbers[2])
print(numbers[4])

# negative indexing
numbers = (10,20,30,40,50)
print(numbers[-1])
print(numbers[-2])
print(numbers[-4])

# slicing
numbers = (10,20,30,40,50)
print(numbers[1:4])
print(numbers[2:])
print(numbers[0:4:2])

# reverse a tuple
numbers = (1,2,3,4,5)
print(numbers[::-1])


#----------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------
"""
                       Tuple Operations
Tuple operations allow us to combine, repeat, search and perform calculations
on tuple elements.
"""

# a) concatenation 
tup_1 = (10,20,30)
tup_2 = (40,50,60)
result = tup_1 + tup_2
print(result)

# b) repetition
data = (1,2,3)
result = data * 3
print(result)

# c) Membership Operators
#      i) in -->
#     ii) not in -->
numbers = (1,2,3,4,5,6)
print(1 in numbers) # True
print(7 in numbers) # False

print(8 not in numbers) # True
print(5 not in numbers)

# Built in functions
# a) len()
numbers = (10,20,30,40)
print(len(numbers))

# b) max()
numbers = (10,20,30,40,50)
print(max(numbers))

# c) min()
numbers = (10,20,30,40,50)
print(min(numbers))

# d) sum()
numbers = (10,20,30,40)
print(sum(numbers))

# e) sorted()
numbers = (40,10,50,30,20)
print(sorted(numbers))   

"""
                        Tuple Methods
Python tuples have two built in methods such as count() and index().
These methods are used to count elements and find the position in a tuple.
"""
# a) count()
numbers = (10,20,30,10,50,30,10,60,70)
result = numbers.count(10)
print(result)

# b) index()
numbers = (10,20,30,40,50)
result = numbers.index(40)
print(result)

data = (10,20,30,10,40,50,10)
print(data.index(10))    # """ the index() method returns the first occurrence, even if the
                         # value appers multiple times. """