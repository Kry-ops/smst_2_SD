class Graph:
    def __init__(self):
        self.adj_list = {}

    def print_graph(self):
        for vortex in self.adj_list:
            print(vortex, ':', self.adj_list[vortex])

my_graph = Graph()
my_graph.print_graph


# demo 1 add vertex
class Graph:
    def __init__(self):
        self.adj_list = {}

    def print_graph(self):
        for vortex in self.adj_list:
            print(vortex, ':', self.adj_list[vortex])
    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False

my_graph = Graph()
my_graph.add_vertex('A')
my_graph.print_graph()


# demo 2 add edge
class Graph:
    def __init__(self):
        self.adj_list = {}

    def print_graph(self):
        for vortex in self.adj_list:
            print(vortex, ':', self.adj_list[vortex])
    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False
    def add_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False

my_graph = Graph()
my_graph.add_vertex('1')
my_graph.add_vertex('2')
my_graph.add_edge('1', '2')
my_graph.print_graph()


# demo 3 remove edge
class Graph:
    def __init__(self):
        self.adj_list = {}

    def print_graph(self):
        for vortex in self.adj_list:
            print(vortex, ':', self.adj_list[vortex])
    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False
    def add_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False
    def remove_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except ValueError:
                pass
            return True
        return False

my_graph = Graph()
my_graph.add_vertex('A')
my_graph.add_vertex('B')
my_graph.add_vertex('C')
my_graph.add_edge('A', 'B')
my_graph.add_edge('B', 'C')
my_graph.add_edge('C', 'A')

print('Graph before remove_edge():')
my_graph.print_graph()

my_graph.remove_edge('A','C')

print('\nGraph after remove_edge():')
my_graph.print_graph()

# demo 4 remove vortex
class Graph:
    def __init__(self):
        self.adj_list = {}

    def print_graph(self):
        for vortex in self.adj_list:
            print(vortex, ':', self.adj_list[vortex])
    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False
    def add_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False
    def remove_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except ValueError:
                pass
            return True
        return False
    def remove_vertex(self, vertex): 
        if vertex in self.adj_list.keys():
            for other_vertex in self.adj_list[vertex]:
                self.adj_list[other_vertex].remove(vertex)
            del self.adj_list[vertex]
        return False
    
my_graph = Graph()
my_graph.add_vertex('A')
my_graph.add_vertex('B')
my_graph.add_vertex('C')
my_graph.add_vertex('D')
my_graph.add_edge('A', 'B')
my_graph.add_edge('A', 'C')
my_graph.add_edge('A', 'D')
my_graph.add_edge('B', 'D')
my_graph.add_edge('C', 'D')

print('Graph bevore remove_vertex():')
my_graph.print_graph()

my_graph.remove_vertex('D')

print('\nGraph nach remove_vertex():')
my_graph.print_graph()