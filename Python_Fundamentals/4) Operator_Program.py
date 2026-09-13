"""
Operators in Python are used to perform operations on variables and values. The main types of operators in Python are:
1. Arithmetic Operators: +, -, *, /, %, **
2. Comparison Operators: ==, !=, <, >, <=, >=
3. Logical Operators: and, or, not
4. Assignment Operators: =, +=, -=, *=, /=, %=, **=
5. Bitwise Operators: &, |, ^, ~, <<, >>
6. Membership Operators: in, not in
7. Identity Operators: is, is not
"""

# Arithmetic Operators---
# a) Addition
a = 10
b = 20
c = a+b
print(f"The Addition of a and b is :- {c}")

# b) Subtraction 
a = 20
b = 10
c = a-b
print(f"The Subtraction of a and b is :- {c}")

# c) Multiplication 
a = 10
b = 5
c = a*b
print(f"The Multiplication of a and b is :- {c}")

# d) Division
a = 20 
b = 5
c = int(a/b)
print(f"The Division of a and b is :- {c}")

# e) Modulus 
a = 20
b = 7
c = a%b
print(f"The Modulus of a and b is :- {c}")

# f) Exponentiation
a = 2
b = 5
c = a**b
print(f"The Exponentiation of a and b is :- {c}")

# g) Floor Division
a = 20
b = 2
c = a//b
print(f"The Floor Division of a and b is :- {c}")

# Comparison Operators---
# a) Equal to
a = 10
b = 20
print(f"The value of a is equal to b :- {a==b}")

# b) Not Equal to 
a = 10
b  = 20
print(f"The value of a is not equal to b :- {a!=b}")

# c) Greater than
a = 10 
b = 20
print(f"The value of a is greater than b :- {a>b}")

# d) Less than
a = 10
b = 20
c = a<b
print(f"The value of a is less than b :-{c}")

# e) Greater than or equal to
a = 10
b = 20
print(f"The value of a is greater than or equal to b :- {a>=b}")

# f) Less than or equal to
a = 10
b = 20
print(f"The value of a is less than or equal to b :- {a<=b}")

# Logical Operators---
# a) and
a = True
b = False
print(f"The value of a and b is :- {a and b}")

# b) or
a = True 
b = False 
print(f"The Value of a or b is :- {a or b}")

# c) not
a = True
print(f"The value of not a is :- {not a}")

# Assignment Operators---
# a) =
a = 10
print(f"The value of a is :- {a}")

# b) +=
a = 10
a += 5
print(f"The value of a after using += operator is :- {a}")

# c) -=
a = 10
a -= 5
print(f"The value of a after using -= operator is :- {a}")

# d) *=
a = 10
a *= 5
print(f"The value of a after using *= operator is :- {a}")

# e) /=
a = 10
a /= 5
print(f"The value of a after using /= operator is :- {a}")

# f) %=
a = 10
a %= 5
print(f"The value of a after using %= operator is :- {a}")

# g) **=
a = 10
a **= 5
print(f"The value of a after using **= operator is :- {a}")

# Bitwise operators---
# a) &
a = 10
b = 20
c = a & b
print(f"The value of a & b is :- {c}")

# b) /
a = 10
b = 20
c = a / b
print(f"The value of a / b is :- {c}")

# c) ^
a = 10
b = 20
c = a ^ b
print(f"The value of a ^ b is :- {c}")

# d) ~
a = 10
c = ~a
print(f"The value of ~a is :- {c}")

# e) <<
a = 10
b = 2
c = a << b
print(f"The value of a << b is :- {c}")

# f) >>
a = 10
b = 2
c = a >> b
print(f"The value of a >> b is :- {c}")


# Membership Operators---
# a) in 
a = "Hello"
b = "H"
print(f"The value of b in a is :- {b in a}")

l = [1,2,3,4,5]
print(f"The value 3 is present in the list :- {3 in l}")

# b) not in 
a = "Hello"
b = "H"
print(f"The value of b not in a is :- {b not in a}")

l = [1,2,3,4,5]
print(f"The value 6 is not present in the list :- {6 not in l}")

# Identity Operators---
# a) is
a = 10
b = 10
print(f"The value of a is b :- {a is b}")

l = [1,2,3]
k = [1,2,3]
print(f"The value of l is k :- {l is k}")

# b) is not
a = 10
b = 20
print(f"The value of a is not b :- {a is not b}")

