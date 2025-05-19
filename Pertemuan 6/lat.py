class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1
    
    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    def push(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1
        return True
    
    def pop(self):
        if self.height == 0:
            return None
        temp = self.top
        self.top = self.top.next
        temp.next =  None
        self.height -= 1
        return temp
    def sisip_stack(self, i, value):
        if i < 0 or i > self.height:
            return False
        pos_from_top = self.height - i
        new_node = Node(value)
        if pos_from_top == 0:
            new_node.next = self.top
            self.top = new_node
        else:
            prev = self.top
            for _ in range(pos_from_top - 1):
                prev = prev.next
            new_node.next = prev.next
            prev.next = new_node
        self.height += 1
        return True


my_stack = stack(4)
my_stack.push(3)
my_stack.push(2)
my_stack.push(1)

print("before pop:")
my_stack.print_stack()

print('\n popped node')
print(my_stack.pop().value)

print('\n after pop')
my_stack.print_stack()

print('\n tes sisip')
my_stack.sisip_stack(1,10)
my_stack.print_stack()