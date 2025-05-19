class Graph:
    def __init__(self):
        self.adj_list = {}

    def print_graph(self):
        for vortex in self.adj_list:
            print(vortex, ':', self.adj_list[vortex])

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []
            return True
        return False

    def add_edge(self, v1, v2):
        if v1 in self.adj_list and v2 in self.adj_list:
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False


my_graph = Graph()

my_graph.add_vertex('52')
my_graph.add_vertex('18')
my_graph.add_vertex('21')
my_graph.add_vertex('44')
my_graph.add_vertex('76')
my_graph.add_vertex('27')
my_graph.add_vertex('82')

my_graph.add_edge('52', '18')
my_graph.add_edge('52', '27')
my_graph.add_edge('18', '44')
my_graph.add_edge('18', '21')
my_graph.add_edge('21', '44')
my_graph.add_edge('21', '76')
my_graph.add_edge('44', '76')
my_graph.add_edge('27', '82')

my_graph.print_graph()
