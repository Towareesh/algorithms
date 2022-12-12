class Graph:
    def __init__(self, graph=None):
        self.graph = graph
        self.symmetry_graph()

    def symmetry_graph(self):
        '''The *experimental method ensures graph symmetry.
        If there is a path from node A to B with the value X,
        then there must be a path from node B to node A with the value X.

        if (A to B = X) in graph:
            if (B to A = X) in graph == False:
                create such a path

        *experimental - not tested, if there is a lack of data about nodes,
        the method may not work correctly.
        '''
        nodes = self.get_nodes()
        for node, path in self.graph.items():
            for adjacent_node, edge in path.items():
                if self.graph[adjacent_node].get(node, False) == False:
                    self.graph[adjacent_node][node] = edge

    def get_nodes(self):
        '''Return the nodes of graph.'''
        nodes = [node for node in self.graph.keys()]
        return nodes

    def get_neighbors(self, node):
        '''Return the node's neighbors.'''
        neighbors = [neighbor for neighbor in self.graph[node].keys()]
        return neighbors

    def get_value(self, node_1, node_2):
        '''Return the value of the edge between two nodes.

        Return a None if the edge value is missing.
        '''
        edge_value = None
        try:
            edge_value = self.graph[node_1][node_2]
        except KeyError:
            pass
        return edge_value


def dijkstra_algorithm(start_node, graph):
    '''Implementation of Dijkstra algorithm.'''
    queue = graph.get_nodes()
    previous_nodes = {}
    shortest_path  = {node: float('inf') for node in queue}
    shortest_path[start_node] = 0
    
    while queue: # algorithm is executed until we visit all nodes
        current_min_node = None
        for node in queue: # finding the node with the lowest score
            if current_min_node == None:
                current_min_node = node
            elif shortest_path[node] < shortest_path[current_min_node]:
                current_min_node = node

        neighbors = graph.get_neighbors(current_min_node)
        for neighbor in neighbors: # updating the values of the edges of the neighbors of the current node
            tentative_value = shortest_path[current_min_node] + graph.get_value(current_min_node, neighbor)
            if tentative_value < shortest_path[neighbor]:
                shortest_path[neighbor] = tentative_value
                previous_nodes[neighbor] = current_min_node # updating the best path to the current node

        queue.remove(current_min_node)

    return shortest_path, previous_nodes

def short_path(graph, start, goal):
    graph = Graph(graph)
    shortest_path, previous_nodes = dijkstra_algorithm(start, graph)
    path = [goal]

    while path[-1] != start:
        path.append(previous_nodes[path[-1]])

    return path[::-1], shortest_path[goal]

graph_1 = {'X1': {'X2': 10, 'X3': 3},
           'X2': {'X1': 10, 'X3': 4},
           'X3': {'X1': 3, 'X2': 4, 'X4': 11},
           'X4': {'X3': 11}}

graph_2 = {'Reykjavik': {'Oslo': 5, 'London': 4},
           'Oslo': {'Berlin': 1, 'Moscow': 3},
           'Moscow': {'Belgrade': 5, 'Athens': 4},
           'London': {},
           'Rome': {'Berlin': 2, 'Athens': 2},
           'Berlin': {},
           'Belgrade': {},
           'Athens': {'Belgrade': 1}}

a = [23, 232, 23]
print(short_path(graph_2, 'Oslo', 'Belgrade'))