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

# example 
names = ['kartik', 'Omkar', 'Suyash', 'Shreya', 'Satish', 'Rudra', 'Dnyaneshwari', 'Gayatri']
for i in names:
    print(i)

# alculate the sum of numbers from 1 to 10.
total = 0
for i in range(1,11):
    total = total+i
print(total)
