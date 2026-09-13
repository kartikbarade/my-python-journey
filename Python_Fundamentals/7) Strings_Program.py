"""
                   String 

String are a sequence of characters written inside quotes.
It include letter,numbers,synbols and spaces. String are immutable in nature.


"""
string = "Hello World!"
print(string)

# Creating a String
# String can be created by enclosing characters inside both single quotes and double quptes.
name = 'Kartik'
name1 = "Yash"
print(name)
print(name1)


#Immutable Strings---
# immutable means we cannot change the value of string once it is created.
# name1 = "Python"
# name1[0] = "M" # This will give an error because strings are immutable

#We can change the value of string by creating a new string and assigning it to the same variable.
name2 = "Python"
name2 = "M" + name2[1:]
print(name2) # Output: Mython


# Indexing in String---
Student_name = "Omkar"
print(Student_name[0])

# Postive Indexing
"""
Positive indexing starts from 0 and goes up to n-1 where n is the length of th string.
"""
language = "Marathi"
print(language[0])
print(language[1])
print(language[2])
print(language[3])
print(language[4])
print(language[5])
print(language[6])

# Negative Indexing
""""
Negative indexing starts from -1 and goes up to -n where n is the length of the string.
"""
language = "Marathi"
print(language[-1])
print(language[-2])
print(language[-3])
print(language[-4])
print(language[-5])
print(language[-6])
print(language[-7])


College_name = input("Enter your college name : ")
print(f"My College name is {College_name}")
print(f"My College 1st letter is {College_name[0]}")


# Slicing ---
""" In Python, slicing means extracting part of a sequence such as a string, list, and tuple
    String Slicing in python is way to get specific parts of a string by using start, end and values(steps).

"""

text = "Hello I'm kartik"
print(text)
print(text[0:3])
print(text[2:])
print(text[0:16:2])
print(text[::3])
print(text[:6:2])
print(text[::-1])
print(len(text)) 

# String Operations
""" Python Provides several operators to work with strings.
    The important ones are :
    1) Concatenation (+)
    2) Repetition (*)
    3) Membership (in, not in)
    4) Comparison Operators 
""" 
    # 1) Concatenation (+)

first_name = "Kartik"
last_name = "Barade"
full_name = first_name + " " + last_name
print(full_name)


    # 2) Repetition (*)

text = "Python"
print(text * 3)

    # 3) membership (in, not in)
state = "Maharashtra"
print("s" in state)

country = "India"
print("k" in country)

animal = "elephant"
print("s" not in animal)
print("e" not in animal)

    # 4) Comparison Operators
    # a) Equal to

a = "Python"
b = "Python"

print(a==b)

    # b) Not equal to
c = "Java"
d = "C"
print(c!=d)


    # c) Greater than 
print("Banana">"Apple")

    # d) Less than
print("Apple"<"Banana")

    # e) Greate than or equal
print("banana">="apple")

    # f) less than or equal
print("apple"<="banana")

"""
Built in string fumctions
    a) len()
    b) max()
    c) min()
    d) sorted()
    e) str()
"""

name = "kartik"
print(len(name))

x = "python"
print(max(x))
print(min(x))

text = "abcXYZ"
print(max(text))
print(min(text))

word = "python"
print(sorted(word))
print(sorted(x,reverse=True)) #desending order

num = "51324"
print(sorted(num))

"""
String Methods 
 i)case conversion method :- These methods are used to change the case of characters in a string.
   a)lower()
   b)upper()
   c)capitalize()
   d)title()
   e)swapcase()
"""

name = "KARTIK BARADE"
result = name.lower()
print(result)

name = "kartik barade"
print(name.upper())


text = "python programming Language"
print(text.capitalize())
print(text.title())


sentence = 'My nAme IS KaRtiK'
print(sentence.swapcase())

"""
  ii) Searching methods :- Searching methods are used to find a character or substring inside a string.
    a) find()
    b) rfind()
    c) index()
    d) count()
"""

text = "Python Programming"
print(text.find("P"))

text = "banana"
print(text.rfind("a"))

text = "Hello Python"
print(text.index("Python"))

word = "banana"
print(word.count("a"))

""" 
  iii) Cheching methods :- checking methods are used to check some condition about a string.
     a) isalpha()
     b) isdigit()
     c) isalnum()
     d) isspace()
     e) islower()
     f) isupper()
"""

# isalpha
text = "Language"
print(text.isalpha())
num = "123"            # Numbers are not alphabets.
print(num.isalpha())
word = "python "       # Space are not alphabets.
print(word.isalpha())

print("Java123".isalpha())

# isdigit
age = "121"
print(age.isdigit())

