from linked_list_zip.linked_list_zip import LinkedList, Node

def test_linked_list():
    ll = LinkedList()
    assert ll.head == None
    
def test_node():
    node = Node(2)
    assert node.value == 2

def test_2_linked_lists():
    ll_1 = LinkedList()
    ll_2 = LinkedList()
    node1 = Node('Reinhardt')
    node2 = Node('DVA')
    ll_1.head = node1
    ll_2.head = node2
    assert ll_1.head.value == 'Reinhardt'
    assert ll_2.head.value == 'DVA'

def test_merge_1_node():
    ll_1 = LinkedList()
    ll_2 = LinkedList()
    
    node1 = Node('Widowmaker')
    node2 = Node('Doomfist')
    
    ll_1.head = node1.value
    ll_2.head = node2.value
    
    ll_1.merge_linked_lists(ll_1, ll_2)
    assert node1.next == node2
    
# def test_merge_nodes():
#     ll_1 = LinkedList()
#     ll_2 = LinkedList()
    
#     node1 = Node('Widowmaker')
#     print(f'node1:{node1}')
#     ll_1.head = node1
    
#     node2 = Node('Doomfist')
#     ll_2.head = node2
#     node3 = Node('Mei')
#     node1.next = node3
#     node4 = Node('Mercy')
#     node2.next = node4
    
#     ll_1.merge_linked_lists(ll_1, ll_2)
#     assert node1.next == 'Mei'
    
