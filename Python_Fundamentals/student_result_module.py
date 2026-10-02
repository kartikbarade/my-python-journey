def student_result():
    print("---------- Enter the all details of student ----------")
    name = input("Enter student name:")
    age = int(input("Enter student age:"))
    college = input("Enter student college name:")
    branch = input("Enter student branch name:")

    print("---------- Enter students marks ----------")
    subject1 = int(input("Enter marks of subject 1:"))
    subject2 = int(input("Enter marks of subject 2:"))
    subject3 = int(input("Enter marks of subject 3:"))

    average = (subject1 + subject2 + subject3) / 3

    print("---------- Student Details ----------")
    print("Name:", name)
    print("Age:", age)
    print("College:", college)
    print("Branch:", branch)
    print("---------- Student Marks ----------")
    print("Subject 1:", subject1)
    print("Subject 2:", subject2)
    print("Subject 3:", subject3)

    print(f"Average Marks of {name} is: {average}")

    if average >= 90:
        print("Grade: A")
    elif average >= 70:
        print("Grade: B")
    elif average >= 50:
        print("Grade: C")
    elif average >= 35:
        print("Grade: D")
    else:
        print("Grade: F")

