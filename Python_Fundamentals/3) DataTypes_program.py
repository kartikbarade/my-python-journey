"""
Data types in Python are used to define the type of data that a variable can hold. The main data types in Python are:
1. Numeric Types: int, float, complex
2. Text Type: str
3. Boolean Type: bool
4. Sequence Types: list, tuple, range
5. Mapping Type: dict
6. Set Types: set, frozenset
7. Binary Types: bytes, bytearray, memoryview

"""
#Numeric Data Types---
# a) Integer
a = 10
print(f"The value of the a is:- {a}")
print(type(a))
b = 20
print(f"The value of the b is:- {b}")
print(type(b))

# b) Float
c = 10.4
print(f"The value of the c is:- {c}")
print(type(c))

# c) Complex
d = 2 + 4j
print(f"The value of the d is:- {d}")
print(type(d))


# Text Data Types---
# # a) String
name = "Kartik"
print(f"The Name of Student is :- {name}")
print(type(name))


# Boolean Type---
is_student = True
print(f"Kartik is a Student of ISBM :- {is_student}")
print(type(is_student))


# Sequence Data Types---
# a) List
marks = [10, 20, 30, 40, 50]
print(f"The marks of students is :- {marks}")
print(marks [2])
print(type(marks))

# b) Tuple 
name = ("Kartik", "Yash", "Omkar")
print(f"The Name of the Students is :- {name}")
print(name [0])
print(type(name))

# c) Range 
mark = range(10)
print(f"The range of the marks is :- {mark}")


# Mapping Data Types---
# a) Dictionary
student = {"Name":"Kartik", "Age": 20, "Course": "AIML"}
print(f"The Student Details is :- {student}")
print(student["Name"])
print(type(student)) 


# Set Data Types---
# a) Set
marks = {10, 20, 30, 40, 50}
print(f"The marks of students is :- {marks}")
print(type(marks))

name = {"Kartik", "Yash", "Omkar"}
print(f"The names of students is :- {name}")
for i in name:
    print(i)

# b) Frozenset
marks = frozenset([10, 20, 30, 40, 50])
print(f"The marks of students is :- {marks}")
print(type(marks))
