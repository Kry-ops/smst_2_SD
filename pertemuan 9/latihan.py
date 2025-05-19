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

    def max_value_node(self, current_node):
        while current_node.right is not None:
            current_node = current_node.right
        return current_node
    
    def average_value_node(self):
        def average(node):
            if node is None:
                return (0, 0) 
            left_total, left_count = average(node.left)
            right_total, right_count = average(node.right)
            total = left_total + node.value + right_total
            count = left_count + 1 + right_count
            return (total, count)
        
        total, count = average(self.root)
        return total / count if count != 0 else 0

    def standard_deviation(self):
        values = []
        stack = []
        current = self.root

    # In-order traversal iteratif
        while stack or current:
            if current:
                stack.append(current)
                current = current.left
            else:
                current = stack.pop()
                values.append(current.value)
                current = current.right

        n = len(values)
        if n == 0:
            return 0

        mean = sum(values) / n
        variance = sum((x - mean) ** 2 for x in values) / n
        return variance ** 0.5  # Akar kuadrat manual

    

my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

print('Minimum value in treee: ')
print(my_tree.min_value_node(my_tree.root).value)
print('Maximum value in treee: ')
print(my_tree.max_value_node(my_tree.root).value)
print('Average value in treee: ')
print(my_tree.average_value_node())
print('standar deviasi in treee: ')
print(my_tree.standard_deviation())