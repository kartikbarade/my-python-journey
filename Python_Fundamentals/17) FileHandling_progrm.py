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

# b) Binary Files
# Binary files store data as bytes.
# They are commonly used for images, audio, video, and other non-text data.
# Examples: .jpg, .png, .mp3, .mp4, .pdf, .exe