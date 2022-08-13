class Node:
    def __init__(self, data, next, prev):
        self.data = data
        self.next = next
        self.prev = prev



class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_beg(self, data):
        self.head = Node(data,self.head,None)
        self.tail = Node(data,None,self.tail)

    def print_forward(self):
        itr = self.head
        ifstr = ''
        while itr:
            ifstr += str(itr.data) + "-->"
            itr = itr.next
        print(ifstr)

    def print_backward(self):
        itr = self.tail
        ibstr = ''
        while itr:
            ibstr += str(itr.data) + "<--"
            itr = itr.prev
        print(ibstr)

d1 = DoublyLinkedList()
d1.insert_at_beg(1)
d1.insert_at_beg(2)
d1.insert_at_beg(3)
d1.print_forward()
d1.print_backward()