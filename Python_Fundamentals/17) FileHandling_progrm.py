"""     ---File Handling---
File handling is the process of creating, opening, reading, 
writing, and closing files using a Python program.

It allows us to store data permanently, even after the program has stopped running.
Example: Saving student names and marks in a file.

"""
# types of files in python 
# a) Text Files :-Text files store data in a human-readable format.
# Examples: .txt, .csv, .py, .html, .json

file = open("student.txt","w")
file.write("Hello Student")
file.write("Name:Kartik")
file.close()

file = open("student.txt","r")
print(file.read())

file = open("sample.txt","r")
print(file.read(50))

file = open("sample.txt","r")
print(file.readline())

file = open("sample.txt","r")
print(file.readline(4))

# using Loop
file = open("sample.txt","r")
for i in file:
    print(i)

file = open("nature.txt","w")
file.write("Nature brings peace to our minds and fills our hearts with happiness and positivity.")
file.write("\nWe should respect and preserve its beauty for future generations.")
file.close()

file = open("nature.txt","r")
print(file.read())
print(file.readline())

   #append file
file = open("nature.txt","a")
file.write("\n")
file.write("\nNature is not a place to visit; it is our home, where life blooms and peace grows.")
file.close()

file = open("nature.txt","r")
for i in file:
    print(i)




#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------
# b) Binary Files
# Binary files store data as bytes.
# They are commonly used for images, audio, video, and other non-text data.
# Examples: .jpg, .png, .mp3, .mp4, .pdf, .exe