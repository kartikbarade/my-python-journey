name = input("Enter your name : ")
maths = float(input("Enter maths marks : "))
Python = float(input("Enter python marks : "))
DSA = float(input("Enter dsa marks : "))

total = maths + Python + DSA
percentage = total / 3

print("---------------------Result--------------------------------")
print("Name = ",name)
print("Total_Marks = ",total)
print("Percentage = ",percentage)

if maths >=40 and Python >=40 and DSA >=40:
    print("Student Pass")

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 75:
        grade = "A"
    elif percentage >= 60:
        grade = "B"
    elif percentage >= 50:
        grade = "C"
    else:
        grade = "D"
    print("Grade : ", grade)

else:
    print("Result       : FAIL")
    print("Grade        : F")