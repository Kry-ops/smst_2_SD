
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
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
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length +=1
        return True

    def resarve_print_list(self):
        temp = self.tail
        while temp is not None:
            print(temp.value)
            temp = temp.prev
    

my_doubly_lingked_list = DoublyLinkedList('jl_selokan_mataram')
my_doubly_lingked_list.append('jl_magelang')
my_doubly_lingked_list.append("jl_pangeran_diponegoro")

print('Rute keberangkatan dari kost ke tugu jogja:')
my_doubly_lingked_list.print_list()

print('\n')
print('------------------------------------------')
print('\n')

print('Rute kepulangan dari tuge jogja ke kost')
my_doubly_lingked_list.resarve_print_list()
# nama_jalan = 
# satu = "jl_selokan_mataram"
# due = "jl_magelang"
# tiga = "jl_pangeran_diponegoro"