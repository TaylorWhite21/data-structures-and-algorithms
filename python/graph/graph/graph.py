from graph.queue import Queue
from graph.stack import Stack


class Graph:
    def __init__(self):
        self.adjacency_list = {}
        # key will be the node, value adj node with a value of the edge

    def __str__(self):
        return self.adjacency_list

    def __repr__(self):
        return self.adjacency_list

    # Adds a node to the graph
    def add_node(self, value):
        vertex = Vertex(value)
        self.adjacency_list[vertex] = []
        return vertex
        # Arguments: value
        # Returns: The added node
        # Add a node to the graph or add to adj list

    def add_edge(self, node1, node2, weight=None):
        if node1 and node2 not in self.adjacency_list:
            raise Exception
        edge1 = Edge(node2, weight)
        self.adjacency_list[node1].append(edge1)

        # Arguments: 2 nodes to be connected by the edge, weight (optional)
        # Returns: nothing
        # Adds a new edge between two nodes in the graph
        # If specified, assign a weight to the edge
        # Both nodes should already be in the Graph

    def get_node(self):
        nodes_in_graph = []
        for i in self.adjacency_list:
            nodes_in_graph.append(self.adjacency_list[i])
        return nodes_in_graph
        # Arguments: none
        # Returns all nodes in graph as a collection (set, list, or similar)

    def get_neighbor(self, vertex):
        list_of_neighbors = []
        vertices = self.adjacency_list[vertex]
        for edge in vertices:
            list_of_neighbors[edge.vertex] = edge.weight

            # Arguments: node
            # Returns a collection of edges connected to the given node
            # Include the weight of connection in returned collection

    def size(self):
        nodes_in_graph = []
        if self.adjacency_list:
            for i in self.adjacency_list:
                nodes_in_graph.append(self.adjacency_list[i])
        else:
            return None
        return len(nodes_in_graph)
        # Arguments: none
        # Returns the total number of nodes in the graph

    def breadth_first(self, vertex):
        nodes = []
        breadth = Queue()
        visited = set()

        breadth.enqueue(vertex)
        visited.add(vertex)

        while breadth.isEmpty() == False:
            front = breadth.dequeue()
            nodes.append(front)

            for child in self.adjacency_list:
                if child not in visited:
                    visited.add(child)
                    breadth.enqueue(child)
        return nodes

    def depth_first(self, vertex):
        if vertex not in self.get_node():
            return []
        result = []
        stack = Stack()
        visited = set()
        stack.push(vertex)
        while stack:
            top = stack.peek()
            if top not in visited:
                result.append(top.value)
            visited.add(top)
            has_unvisted = False
            children = []
            for edge in self.get_neighbors(top):
                children.append(edge.vertex)
            for child in children:
                if child not in visited:
                    has_unvisited = True
                    stack.push(child)
                    break
            if not has_unvisited:
                stack.pop()
        return result


class Vertex:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value

    def __repr__(self):
        return self.value


class Edge:
    def __init__(self, vertex, weight=0):
        self.vertex = vertex
        self.weight = weight

    def __repr__(self):
        return self.vertex
