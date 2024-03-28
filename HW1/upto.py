'''
    PIC 16A Homework 1
    Author: Jiayu Li
    UID: 605348766
    Date: 01/20/2023
'''

def squareUpTo(n):
    list = []
    for i in range(n+1):  # 错误的没有考虑n+1
        if i ** 2 <= n:
            list.append(i**2)
    return list

print(squareUpTo(1))
print(squareUpTo(10))
print(squareUpTo(100))

# solution 1
def squareUpTo(n):
  l = []
  i = 0
  while i**2 <=n:
    l.append(i**2)
    i+=1 
  return l

# solution 2
import math
def squareUpTo(n):
  # you can google math.sqrt and math.floor
  return [i**2 for i in range(0, math.floor(math.sqrt(n))+1)]

# solution 3
def squareUpTo(n):
  # less efficient compared with solution 2, since we need n+1 iterations
  return [i**2 for i in range(0, n+1) if i**2 <=n]
