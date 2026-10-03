"""
Task
The provided code stub reads and integer, 'n', from STDIN. 
For all non-negative integers 'i < n', print 'i²'.

Example:-
If n = 3, the output should be:
0
1
4
"""

# code ----->
if __name__ == '__main__':
    n = int(input())
    
for i in range(n):
    sqrt = i * i
    print(sqrt)