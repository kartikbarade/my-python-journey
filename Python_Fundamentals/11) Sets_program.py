"""
A set in Python is an unordered collection of unique elements. Sets are used to store 
multiple values in a single variable, and they automatically remove duplicate elements
Sets are mutable, meaning we can add or remove elements after creating them. Sets are
written using curly brackets {}.
"""
# Example
set = {10,20,'pune',30,40,50,'kartik'}
print(set)

# Characteristics
# a) unorder
data = {30,10,20,40} # Sets do not maintain a order of elements.
print(data)

# b) Unique elements
data = {10,20,50,10,40,10,30}  # avoid duplicates
print(data)

# c) mutable
data = {10,20,30}  # We can add or remove elements from a set after creating it.
data.add(40)
print(data)

# d) no indexing
data = {10,20,30,40,50}
# print(data[0])  # type error

# e) Heterogeneous Elements
student_data = {10,'Pune',9.14,"kartik",30}  #A set can contain different data types
print(student_data)

# f) No duplicate values
numbers = {1,1,1,2,3,4,5,1,2}
print(numbers)

#----------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------
# Creating sets
"""
In python, we can create sets in 3 different ways.
         a) using curly braces{}
         b) using sets constructor set()
         c) Creating an empty sets
"""

# a) using curly braces{}
numbers = {10,20,30,40}
print(numbers)
# b) using sets constructor set()
# numbers = set([10, 20, 30, 20, 10])
# print(numbers)
# my_set = set("Python")
# print(my_set)

# c)Creating an Empty Set
# emptyset = set()
# print(emptyset)

#----------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------
# Adding and Removing Elements
#  a) adding elements
#    i) add() method
numbers = {10,20,30}
numbers.add(40)
print(numbers)

#    ii) update() method
numbers = {10,20,30}
numbers.update([40,50,60])
print(numbers)

# b) removing elements
#     i)remove()
numbers = {10,20,30,40}
numbers.remove(20)
print(numbers)

#     ii)discard()
numbers = {10,20,30,40}
numbers.discard(20)
print(numbers)

numbers = {10,20,30,40}
numbers.discard(50)
print(numbers)


#      iii)pop()
numbers = {40,10,20,30}
numbers.pop()
print(numbers)

data = {1,2,3,4}
removed = data.pop()
print("Removed :", removed)
print(data)

#      iv) clear()
numbers = {1,2,3,4,5}
numbers.clear()
print(numbers)


#----------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------
# Set Operators
# a) union()
a = {1,2,3,4,5}
b = {4,5,6,7,8}
result = a.union(b)
print(result)
print(a|b)    # using | operator

# b) difference
a = {1,2,3,4,5}
b = {4,5,6,7,8}
result = a.difference(b)
print(result)
print(a - b)  # using - operator

# c) symmetric difference
a = {1,2,3,4,5}
b = {4,5,6,7,8}
result = a.symmetric_difference(b)
print(result)
print(a ^ b)  # using ^operator

# d) intersection
a = {1,2,3,4,5}
b = {4,5,6,7,8}
result = a.intersection(b)
print(result)
print(a & b)  # using & operator

#----------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------
# Set Methods
# a) copy()
a = {1,2,3}
b = a.copy()
print(b)

# b) isdisjoint()
a = {1,2,3}
b = (4,5,6)
print(a.isdisjoint(b))

c = {1,2,3}
d = {3,4,5}
print(c.isdisjoint(d))

# c) issubset()
a = {1,2,3}
b = {1,2,3,4,5,6}
print(a.issubset(b))

# d) issuperset()
a = {1,2,3,4,5,6}
b = {1,2,3}
print(a.issuperset(b))

# e) update()
a = {10,20,30}
b = {40,50,60}
a.update(b)
print(a)

# f) intersection_update()
a = {1,2,3,4}
b = {3,4,5,6}
a.intersection_update(b)
print(a)

# g) difference_update()
a = {1,2,3,4}
b = {3,4,5,6}
a.difference_update(b)
print(a)

# h) symmetric_difference_update
a = {1,2,3,4}
b = {3,4,5,6}
a.symmetric_difference_update(b)
print(a)