class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1
    
    def print_queue(self):
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    def enqueue(self, value):
        new_node = Node(value)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1
        return True
    
    def dequeue(self):
        if self.length == 0:
            return None
        temp = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            temp.next = None
        self.length -= 1
        return temp
    
    
    def desperation(self, index):
        if index <= 0 or index > self.length:
            return None
        temp = self.length - index
        if temp == 0:
            return self.dequeue()
        prev = self.first
        for _ in range(temp - 1):
            prev = prev.next
        removed = prev.next
        prev.next = removed.next
        if removed == self.last:
            self.last = prev
        removed.next = None
        self.length -= 1
        return removed


print('awal')
my_queue = queue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)
my_queue.enqueue(4)
my_queue.enqueue(5)
my_queue.print_queue()

print('\n menghapus index ke 1 dan 3:')
print(my_queue.desperation(3).value)  
print(my_queue.desperation(1).value)  


print('\n hasil')
my_queue.print_queue()  