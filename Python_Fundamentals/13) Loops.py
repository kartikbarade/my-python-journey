"""      Loops in Python      """
# 1) What is Iteration
"""Iteration means repeating a set of instructions multiple times until a particular 
condition is satisfied or until all items in a collection have been processed."""

# Suppose we want to print "Hello World" 5 times 
   # without loop
print("Hello World")
print("Hello World")
print("Hello World")
print("Hello World")
print("Hello World")

   # with loop
print("#-------------#")
for i in range(5):
    print("Hello World")

# 2) What is Loop
"""A loop is a programming structure that allows us to execute a block of code repeatedly.
Python mainly provides two types of loops:
       a) for loop
       b) while loop
"""
# a) for loop
for i in range (5):
    print(i)

# b) While loop
i = 1
while i<=5:
    print(i)
    i+=1

# Example ----
names = ['kartik', 'Omkar', 'Suyash', 'Shreya', 'Satish', 'Rudra', 'Dnyaneshwari', 'Gayatri']
for i in names:
    print(i)

# alculate the sum of numbers from 1 to 10.
total = 0
for i in range(1,11):
    total = total+i
print(total)

#----------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------
# for loop
"""
              for loop
A for loop is used to repeat a block of code for each item in a sequence or iterable.
It is commonly used with :
            range(), lists,tuples,sets,dictionaries.

- Syntax : for variable in sequence
               statements
"""
# Examples -----
for i in range(1,6):
    print(i)

num = int(input("Enter a number"))  # user define number
for i in range(num):
    print(i)

fruits = ['Mango', 'Apple', 'Banana', 'Grapes']  # Lists
for i in fruits: 
    print(i)

fruits = ['Mango', 'Apple', 'Banana', 'Grapes'] 
fruits[1]='Orange'
for i in fruits: 
    print(i)

fruits = ['Mango', 'Apple', 'Banana', 'Grapes']  
fruits.append('Kiwi')
for i in fruits:
    print(i)

fruits = ['Mango', 'Apple', 'Banana', 'Grapes']  
fruits.insert(2,'Watermelon')
for i in fruits:
    print(i)

fruits = ['Mango', 'Apple', 'Banana', 'Grapes']  
fruits.pop(2)
for i in fruits:
    print(i)

name = "Kartik"  # String
for i in name:
    print(i)

student_data = ("kartik", 101,"AIML","Pune",9.14) # Tuple
for i in student_data:
    print(i)

branch = {'Comp', 'IT', 'AIML', 'AIDS', 'Mech', 'Elec'}  #Sets
for i in branch:
    print(i)

student = {"name":"kartik","rollno":13,"branch":"AIML"}  # Dictionaries
for key,value in student.items():
    print(f"{key},{value}")

