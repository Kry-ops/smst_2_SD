class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def reverse(self):
        prev = None
        current = self.head
        self.tail = self.head 
        
        while current is not None:
            next_node = current.next  
            current.next = prev
            prev = current 
            current = next_node 
        self.head = prev

print('Kondisi awal')
my_linked_list = LinkedList(23)
my_linked_list.append(43)
my_linked_list.append(12)
my_linked_list.append(71)
my_linked_list.append(87)
my_linked_list.print_list()


print('\nKondisi akhir')
my_linked_list.reverse()
my_linked_list.print_list()