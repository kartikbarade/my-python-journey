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


