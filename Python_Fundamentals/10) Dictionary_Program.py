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