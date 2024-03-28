class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def __eq__(self, other):
        return self.data == other.data
    def __str__(self):
        return str(self.data)
    def __repr__(self):
        return 'Node(' + repr(self.data) + ')'
    def set_next(self, next_node):
        self.next = next_node
    
class LinkedList:
    def __init__(self, init_list = None):
        # be careful with init_list = []
        self.first = None
        self.last = None
        self.len = 0
        if init_list:
            for data in init_list:
                self.append(data)
    def append(self, data):
        new_node = Node(data)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.len += 1
    def prepend(self, data):
        new_node = Node(data)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            new_node.next = self.first
            self.first = new_node
        self.len += 1
    def __len__(self):
        return self.len
        
    def __eq__(self, other):
        if len(self) != len(other):
            return False
        node1 = self.first
        node2 = other.first
        while node1 is not None:
            if node1.data != node2.data:
                return False
            node1 = node1.next
            node2 = node2.next
        return True
    def __str__(self):
        '''
        __str__ is in general flexible. 
        You will be fine as long as it print in a human-friendly way.
        It's preferable to store the strings in a list and then concatenate them 
with "join",
        other than using "+" one by one.
        '''
        result = []
        nodes = self.first
        while nodes is not None:
            result.append(repr(nodes.data))
            nodes = nodes.next
        return "[" + ' -> '.join(result) + " -> ]"
    ## You can define __iter__ and __next__ in the following way
    # def __iter__(self):
    #     self.current = self.first
    #     return self
    # def __next__(self):
    #     if self.current is None:
    #         raise StopIteration
    #     else:
    #         data = self.current.data
    #         self.current = self.current.next
    #         return data
    ## You can also define __iter__ and generator in the following way
    ## The generator may be easier to implement
    def __iter__(self):
        return self.generator()
    def generator(self):
        current = self.first
        for _ in range(self.len):
          yield current.data
          current = current.next
        
if __name__ == "__main__":
    LL = LinkedList(['8', [8], [8], '8'])
    LL.append(1)
    LL.append(2)
    LL.append(3)
    LL.prepend(-1)
    LL.prepend(-2)
    LL.prepend(-3)
    print(LL)
    print(len(LL))
    for i in LL:
        print(i, end = " ")
    print("")
    for i in LL:
        print(i, end = " ")
    print("")