class Node:
    def __init__(self, data= None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beg(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def insert(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_len(self):
        c = 0
        itr = self.head
        while itr:
            c += 1
            itr = itr.next
        return c

    def remove_at(self, index):
        if index < 0 or index > self.get_len():
            raise Exception("Invalid index")
        if index == 0:
            self.head = self.head.next
            return

        itr = self.head
        c = 0
        while itr:
            c += 1
            if c == index-1:
                itr.next = itr.next.next
                break
            itr = itr.next

    def insert_at(self, index, data):
        if index<0 or index>=self.get_len():
            raise Exception("invalid index")
        if index == 0:
            self.head = Node(data,self.head)
        c = 0
        itr = self.head
        while itr:
            if c == index-1:
                itr.next = Node(data, itr.next)
            c += 1
            itr = itr.next

    def get_index_of_val(self, data):
        itr = self.head
        c = 0
        flag = 0
        while itr:
            c += 1
            if itr.data != data:
                pass
            else:
                flag = 1
                break
            itr = itr.next
        if flag == 0:
            raise Exception("Invalid Data, not present in linked list")
        else:
            return c

    def insert_after_val(self, data, val):
        self.insert_at(self.get_index_of_val(data), val)

    def remove_by_val(self, data):
        self.remove_at(self.get_index_of_val(data))

    def print_llist(self):
        if self.head is None:
            print('Linked list is empty')
            return

        itr = self.head
        lstr = ''

        while itr:
            lstr += str(itr.data) + '-->'
            itr = itr.next
        print(lstr)


if __name__ == '__main__':
    l1 = LinkedList()
    l1.insert(["banana","mango","grapes","orange"])
    l1.print_llist()
    l1.insert_after_val("mango","apple")
    l1.print_llist()
    l1.remove_by_val("orange")
    l1.print_llist()
    # l1.remove_by_val("figs")
    # l1.print_llist()
    l1.remove_by_val("banana")
    l1.remove_by_val("mango")
    l1.remove_by_val("apple")
    l1.remove_by_val("grapes")
    l1.print_llist()


    # a = LinkedList()
    # a.insert_at_beg(8)
    # a.insert_at_beg(76)
    # a.insert_at_end(9)
    # # a.insert_at([1,2,3,34])
    # a.print_llist()
    # a.remove_at(2)
    # a.print_llist()
    # a.insert_at(1,100)
    # a.print_llist()