name = "kartik"
print(type(name))

age = 21
print(type(age))

marks = 90.5
print(type(marks))

student = type(
    "Student",(),{
        "name": "Kartik",
        "age":21
    }
)
student1 = student() 
print(student1.name)
print(type(student1.name))
print(student1.age)

x = 10
y = float(x)
print(y)
print(type(y))

num ="123"
s = int(num)
print(s)
print(type(s))


l = 12.4
k = 23.5

m = int(l) + int(k)
print("The addition is : ",m)


marks = 72.7
marks = int(marks)
print(marks)

age = 10
age = bool(age)
print(age)
