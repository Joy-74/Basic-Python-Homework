'''
    PIC 16A Homework 3
    Author: Jiayu Li
    UID: 605348766
    Discussion Section: 3B
    Date: 02/05/2023
'''

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

    def __eq__(self, other):
        return self.data == other.data
    
    def __str__(self):
        return str(self.data)
    
    def __repr__(self):
        return f"Node({self.data})"
    
    def set_next(self, other_node):
        self.next = other_node


    
n = Node(10)

# Test
print(Node(10) == Node(10))
print(Node([10]) == Node([10]))
print(Node([11]) == Node([10]))
print(str(n))
print(repr(n))
print(eval(repr(n)) == n)

m = Node(20)
n.set_next(m)
print(n.next)

m = Node([20])
n.set_next(m)
print(n.next)


# solution
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def __eq__(self, other):
        return self.data == other.data
    def __str__(self):
        # it's OK to write str(self.data),  flexible
        return repr(self.data)
    
    def __repr__(self):
        # It must be repr(self.data), not str(self.data)
        # test eval(repr(n)) == n with n.data = "8"
        return 'Node(' + repr(self.data) + ')'
    def set_next(self, other):
        self.next = other