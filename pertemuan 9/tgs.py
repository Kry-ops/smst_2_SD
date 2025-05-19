class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while (True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self, value):
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
            return False

    def min_value_node(self, current_node):
        while current_node.left is not None:
            current_node = current_node.left
        return current_node

    def reconstruct(self, value):
        stack = []
        parent = None
        node = self.root
        while node:
            if value < node.value:
                parent = node
                node = node.left
            elif value > node.value:
                parent = node
                node = node.right
            else:
                if node.left is None or node.right is None:
                    child = node.left if node.left else node.right
                    if parent is None:
                        self.root = child
                    elif parent.left == node:
                        parent.left = child
                    else:
                        parent.right = child
                else:
                    min_parent = node
                    successor = node.right
                    while successor.left:
                        min_parent = successor
                        successor = successor.left
                    node.value = successor.value
                    if min_parent.left == successor:
                        min_parent.left = successor.right
                    else:
                        min_parent.right = successor.right
                break
        values = []
        stack = []
        current = self.root
        while stack or current:
            if current:
                stack.append(current)
                current = current.left
            else:
                current = stack.pop()
                values.append(current.value)
                current = current.right
        if not values:
            self.root = None
            return
        mid_stack = [(0, len(values) - 1, None, True)]
        self.root = None
        nodes = [None] * len(values)
        while mid_stack:
            left, right, parent_idx, is_left = mid_stack.pop()
            if left > right:
                continue
            mid = (left + right) // 2
            node = Node(values[mid])
            nodes[mid] = node
            if parent_idx is None:
                self.root = node
            else:
                if is_left:
                    nodes[parent_idx].left = node
                else:
                    nodes[parent_idx].right = node
            mid_stack.append((mid + 1, right, mid, False))
            mid_stack.append((left, mid - 1, mid, True))


my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

print('Minimum value in tree: ')
print(my_tree.min_value_node(my_tree.root).value)

my_tree.reconstruct(21)
print("\nHasil setelah reconstruct (hapus 21):")
stack = []
current = my_tree.root
while stack or current:
    if current:
        stack.append(current)
        current = current.left
    else:
        current = stack.pop()
        print(current.value)
        current = current.right
