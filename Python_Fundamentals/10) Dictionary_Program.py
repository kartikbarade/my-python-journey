""" 
                     Dictionary 
A dictionary in Python is a built-in data structure used to store data 
in the form of key-value pairs.
Each key is unique and is used to access its corresponding value. Dictionaries are mutable, 
meaning we can add, update, and delete items after creating them.
"""
student = {
      "name" : "Kartik",
      "age" : 21,
      "branch" : "AIML"
}
print(student)

# 1) Definition : A dictionary is an unordered collection of data stored as key-value pairs.

student_data = {
     "name" : "Kartik",
     "age" : 21,
     "address" : "Pune",
     "Stu_ID" : 101,
     "Branch" : "AIML"
}
print(student_data)

#----------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------

# 2) key value Pair concept : 
""" A dictionary stores in two parts :
             a) key : A unique identifier used to access a value.
             b) value : The data associated with the key.   
"""
student_data = {
     "name" : "Kartik",
     "age" : 21
}
print(student_data["name"])
print(student_data["age"])

#----------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------
# 3) Accesiing Dictionary Elements
# a) accessing dictionary elements using keys[]
student_data = {
     "name" : "Kartik",
     "age" : 21,
}
print(student_data["name"])
print(student_data["age"])

# b) using the get() method
student_data = {
     "name" : "Kartik",
     "age" : 21,
}
print(student_data.get("name"))
print(student_data.get("age"))

     # accessing the Missing key

student_data = {
    "name" : "Kartik"
}
print(student_data.get("age"))

     # using default value
student_data = {
    "name" : "Kartik"
}
print(student_data.get("age","Not Available"))

#----------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------
# 4) Modifying dictionary in Python
# a) adding elements to a dictionary
student = {
    "name" : "kartik",
    "age" : 21
}
print(student)
student["branch"] = "AIML"  # here we add new data (new key-value pair)
print(student)

# b) Updating Values in a Dictionary
student = {
    "name" : "kartik",
    "age" : 21
}
print(student)
student["age"] = 22 # value is updated to 22
print(student)

# c) update() method
student = {
    "name" : "kartik",
    "age" : 21
}
student.update({"branch":"AIML"}) # adding new element
print(student)

student = {
    "name" : "kartik",
    "age" : 21
}
student.update({"age":22})  # Updating Existing Values
print(student)

student = {
    "name" : "Omkar",
    "age" : 21
}
student.update({
    "age" : 22,
    "branch" : "AIML",
    "Address" : "Latur",
    "Friend" : "Kartik"
})
print(student)

#----------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------
# 5) Removing Methods
# a) pop() method
student = {
    "name" : "kartik",
    "age" : 21,
    "branch" : "AIML"
}
result = student.pop("branch")
print(result)
print(student)

employee = {
    "name" : "satish",
    "emp_id" : 101
}
print(student.pop("salary","Not found"))  # using default value

# b) popitem() method
student = {
    "name" : "kartik",
    "age" : 21,
    "branch" : "AIML"
}
result = student.popitem()
print(result)
print(student)

# c) del keyword
student = {
    "name" : "kartik",
    "age" : 21,
    "branch" : "AIML"
}
del student["age"]
print(student)

# d) clear method
student.clear
print(student)