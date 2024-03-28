'''
    PIC 16A Homework 4
    Author: Jiayu Li
    UID: 605348766
    Discussion Section: 3B
    Date: 02/08/2023
'''


class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        s = ''
        if type(self.data) != type(''):  # the object 'data' is not string
            s = str(self.data)
        else:  # the object 'data' is string
            s = "'" + str(self.data) + "'"
        return s


class LinkedList(object):
    def __init__(self, init_list=None):
        self.first = self.last = None
        self.len = 0
        if init_list:
            for data in init_list:
                self.append(data)

    def append(self, data):
        new_node = Node(data)
        if self.first:
            self.last.next = new_node
            self.last = new_node
        else:  # self.first, self.last is None
            self.first = self.last = new_node
        self.len += 1

    def prepend(self, data):
        new_node = Node(data)
        if self.first:
            new_node.next = self.first
            self.first = new_node
        else:  # self.first, self.last is None
            self.first = self.last = new_node
        self.len += 1

    def __len__(self):
        return self.len

    def __eq__(self, other):
        if self.len != other.len:
            return False

        x = self.first
        y = other.first
        while True:
            if not x:
                return True
            if x.data != y.data:
                return False
            x = x.next
            y = y.next

    def __str__(self):
        s = '['
        x = self.first
        while x:
            s += str(x)
            s += ' -> '
            x = x.next
        s += ']'
        return s


    def __iter__(self):
        self.current_node = self.first
        return self

    def __next__(self):
        if self.current_node:
            node = self.current_node
            self.current_node = self.current_node.next
            return node
        else:
            raise StopIteration


# Test

LL = LinkedList([-1, 1])
print(len(LL))

Lempty = LinkedList()
L01 = LinkedList([0, 1])
L02 = LinkedList([0, 1])
L1 = LinkedList([1])
print(Lempty == L01, L01 == L02, L01 == L1)

LL = LinkedList(['8', [8], [8], '8'])
LL.append(1)
LL.append(2)
LL.append(3)
LL.prepend(-1)
LL.prepend(-2)
LL.prepend(-3)
print(LL)

a = LinkedList([0])
a.append(1)
a.append(2)

for n in a:
    print(n, end=" ")
for n in a:
    print(n, end=" ")

