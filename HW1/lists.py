'''
    PIC 16A Homework 1
    Author: Jiayu Li
    UID: 605348766
    Date: 01/17/2023
'''

L = [[i for i in range(j)] for j in range(1,6)]
print(L)


L = [i for j in range(6) for i in range(j)]
print(L)


L = [i for i in range(10,40)
    if i % 5 == 0]
print(L)

print([i*5 for i in range(2,8)])


L = [i for i in range(65,5,-1)
    if i % 5 == 0 and i % 10 != 0]
print(L)

print([i*5 for i in range(13,1,-2)])
