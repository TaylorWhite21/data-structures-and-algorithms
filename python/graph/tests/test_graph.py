from graph.graph import *

# Node can be successfully added to the graph
# def test_add_node():
#     graph = Graph()
#     node1 = graph.add_node('Yoshi')
#     assert node1 in graph.adjacency_list[1][0]

# # An edge can be successfully added to the graph
# # def test_add_edge():
# #     graph = Graph()
# #     node1 = graph.add_node('Reinhardt')
# #     node2 = graph.add_node('Yoshi')
# #     edge = graph.add_edge(node1, node2, 'Halo')
# #     assert edge.weight == 'Halo'
    
# # A collection of all nodes can be properly retrieved from the graph
# def test_get_node():
#     graph = Graph()
#     node1 = graph.add_node('Cloud')
#     node2 = graph.add_node('Tifa')
#     node3 = graph.add_node('Yuffie')
#     actual = graph.get_node()
#     expected = [['Cloud'], ['Tifa'], ['Yuffie']]
#     assert actual == expected
    
    
# # All appropriate neighbors can be retrieved from the graph
# # Neighbors are returned with the weight between nodes included
# # The proper size is returned, representing the number of nodes in the graph
# def test_get_size():
#     graph = Graph()
#     node1 = graph.add_node('Cloud')
#     node2 = graph.add_node('Tifa')
#     node3 = graph.add_node('Yuffie')
#     actual = graph.size()
#     expected = 3
#     assert actual == expected
    
# # A graph with only one node and edge can be properly returned
# # def test_add_node():
# #     graph = Graph()
# #     node1 = graph.add_node('Yoshi')
# #     # print(f'in test: {graph.adjacency_list}')
# #     assert node1 in graph.adjacency_list[1][0]

# # An empty graph properly returns null
# def test_get_size_empty():
#     graph = Graph()
#     actual = graph.size()
#     expected = None
#     assert actual == expected
# # Ensure your tests are passing before you submit your solution.
    
    
def test_breadth_first():
    graph = Graph()
    node1 = graph.add_node('Junkrat')
    node2 = graph.add_node('Widowmaker')
    node3 = graph.add_node('Hanzo')
    node4 = graph.add_node('Tracer')
    actual = graph.breadth_first(node1)
    expected = ['Junkrat', 'Widowmaker', 'Hanzo', 'Tracer']
    assert actual == expected
