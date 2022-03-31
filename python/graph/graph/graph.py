class Graph:
  
    def __init__(self):
        self.adjacency_list = {}
        self.dict_key = 1
        # key will be the node, value adj node with a value of the edge

    # Adds a node to the graph
    def add_node(self, value):
        v = Vertex(value)
        self.adjacency_list[self.dict_key] = list()
        self.adjacency_list[self.dict_key].append(v.value)
        self.dict_key += 1
        # print(f'dict_key: {self.dict_key}')
        # print(f'in add node: {self.adjacency_list}')
        # print(v.value)
        return self.adjacency_list[self.dict_key - 1][0]
            # Arguments: value
            # Returns: The added node
            # Add a node to the graph or add to adj list

    # def add_edge(self, node1, node2, weight=None):
    #   print(self.adjacency_list)
    #   edge1 = Edge(node2, weight)
    #   self.adjacency_list[node1].append(edge1)
      
            # Arguments: 2 nodes to be connected by the edge, weight (optional)
            # Returns: nothing
            # Adds a new edge between two nodes in the graph
            # If specified, assign a weight to the edge
            # Both nodes should already be in the Graph

    def get_node(self):
      nodes_in_graph = []
      for i in self.adjacency_list:
        nodes_in_graph.append(self.adjacency_list[i])
      # print(f'nodes in graph: {nodes_in_graph}')
      return nodes_in_graph
            # Arguments: none
            # Returns all nodes in graph as a collection (set, list, or similar)

    def get_neighbor(self):
        pass
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
      print(nodes_in_graph)
      return len(nodes_in_graph)
            # Arguments: none
            # Returns the total number of nodes in the graph


class Vertex:
    def __init__(self, value):
        self.value = value
    def __repr__(self, vertex):
      self.vertex = vertex
      return self.vertex

class Edge:
    def __init__(self,vertex, weight=None):
        self.vertex = vertex
        self.weight = weight
    def __repr__(self, vertex):
      self.vertex = vertex
      return self.vertex
