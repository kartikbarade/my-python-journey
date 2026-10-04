"""
Problem statement :-
You are given three integers x, y, and z, representing the dimensions of a 3D grid,
and an integer n.

Your task is to print a list of all possible coordinates [i, j, k] on the grid where:
0≤i≤x
0≤j≤y
0≤k≤z

However, you must exclude all coordinates where the sum of the coordinates is equal to n.
The result should be generated using list comprehension.
"""
# code ----->
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    result = [[i,j,k] 
              for i in range (x + 1)
              for j in range (y + 1)
              for k in range (z + 1)
              if i+j+k != n]
    print(result)