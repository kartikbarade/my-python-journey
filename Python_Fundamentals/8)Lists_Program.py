"""
-------------------Lists-----------------------
A List in python is a collection data type used to store multiple values/elements in a single
variable.
Lists are one of the most commonly used data structures in python.
A list is an ordered,mutable collection of elements enclosed in square brackets [].

"""
# simple example
fruits = ["Apple","Banana","Mango"]
print(fruits)
# Ordered lists
number = [10,20,30,40]
print(number)
# mutable lists
numbers = [10,20,30,40,50]
numbers [2] = 70
print(numbers)
# Duplicate Values
numbers = [10,20,10,30,40,20]
print(numbers)
# Allows different data types
data = [10,"Python",3.14,True]
print(data)

#----------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------#
#Accessing list elements
"""
In python, accessing list elements means retrieving or using individual values stored inside a list.
   1) Indexing(Positive and Negative)
   2) slicing
   3) Accessing nested list
   4) using len() function
"""
# 1) Indexing(Positive and Negative)
fruits = ["Apple","Mango","Orange","Banana","Grapes"]
print(fruits)
print(fruits[0])
print(fruits[2])
print(fruits[-1])
print(fruits[-3])

# 2) Slicing
numbers = [10,20,30,40,50]
print(numbers[1:4])
print(numbers[:3])
print(numbers[2:])
print(numbers[0:5:2])
print(numbers[::-1]) # reverse list using slicing

# 3) Accessing nested list
numbers = [[10,20],[30,40],[50,60]]
print(numbers[1])
print(numbers[2][0])

# 4) using len() function
numbers = [10,20,30,40,50]
print(len(numbers))

#----------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------#
#Modifying Lists
"""
Modifying lists:-
Modifying a list means changing the contents of an existing list.
since python lists are mutable, we can-
        1) Changing existing elements
        2) Add new elements
        3) Remove elements
"""
# 1) Changing existing elements
numbers = [10,20,30,40]
print(numbers)
numbers [1] = 200
print(numbers)

data = [1,2,3,4,5,6] # Multiple elements can also be change
data [1:4] = [2.1,3.1,4.1] 
print(data)

#----------------------------------------------------------------------------------------------#
# 2) Adding Elements
  # a) append
number = [1,2,3]
number.append(4)
print(number)

data = [10,20,30,40] # append() adds only object/elements
data.append([50,60]) # [50,60] becomes 1 elements
print(data)

  # b) insert
number = [100,200,300]
number.insert(1,600)
print(number)

data = ["kartik",21,"Pune",12200]
data.insert(2,["ISBM","AIML"])
print(data)

  # c) extend()
team = ["Shreya","Omkar","kartik"]
print(team)
team.extend(["suyash","rudra","satish"]) # here the elements suyash,rudra,satish are addded individually.
print(team)

#----------------------------------------------------------------------------------------------#

