# 1) Find the Sum of All Elements
elements = [10,20,30,40]
element = sum(elements)
print(element)

# 2) Find the Largest Number
elements = [20,46,82,48,29]
element = max(elements)
print(element)

# 3) Reverse a List
list = [1,2,3,4]
print(list[::-1])

# 4) Count Even and Odd Numbers
list = [1,2,3,4,5,6]

even =0
odd = 0
for i in list:
    if i % 2==0:
        even +=1
    else:
        odd +=1
print(even)
print(odd)

