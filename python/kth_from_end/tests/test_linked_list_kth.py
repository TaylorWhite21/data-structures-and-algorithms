from linked_list_kth.linked_list_kth import LinkedList, Node
import pytest

def test_kth_from_end():
    ll = LinkedList()
    node1 = Node('Master Chief')
    ll.head = node1
    node2 = Node('Cortana')
    node1.next = node2
    node3 = Node('Noble 6')
    node2.next = node3
    node4 = Node('Samuel-034')
    node3.next = node4
    assert  ll.kth_from_end(3) == 'Master Chief'
    

# @pytest.mark.skip('pending')
# If k is greater than length of linked list?
def test_k_is_greater_than_list(self):
    ll = LinkedList()
    node1 = Node('Master Chief')
    ll.head = node1
    node2 = Node('Cortana')
    node1.next = node2
    node3 = Node('Noble 6')
    node2.next = node3
    # assert ll.kth_from_end(5) == 'Kth is longer than linked list'
    self.assertRaises(Exception)

# What if k is the same length as the list?
# Return the Head
def test_k_same_length_as_list():
    ll = LinkedList()
    node1 = Node('Master Chief')
    ll.head = node1
    node2 = Node('Cortana')
    node1.next = node2
    node3 = Node('Noble 6')
    node2.next = node3
    node4 = Node('Samuel-034')
    node3.next = node4
    assert ll.kth_from_end(3) == ll.head.value


# What if k is not a positive integer?
def test_k_is_negative(self):
    ll = LinkedList()
    node1 = Node('Master Chief')
    ll.head = node1
    node2 = Node('Cortana')
    node1.next = node2
    node3 = Node('Noble 6')
    node2.next = node3
    node4 = Node('Samuel-034')
    node3.next = node4
    self.assertRaises(Exception)

# What if the linked list is a size of 1?
def test_list_size_1():
    ll = LinkedList()
    node1 = Node('Master Chief')
    ll.head = node1
    assert ll.kth_from_end(1) == 'Master Chief'
