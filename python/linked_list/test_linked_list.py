from linked_list import LinkedList, Node
import pytest

def test_node_instance():
  node = Node(2, None)
  assert node.next == None
  assert node.value == 2

def test_node_instance_fail():
  node = Node(1, None)
  assert node.next != node
  assert node.value != 2
  
def test_linked_list():
  node = Node(1, None)
  ll = LinkedList(node)
  assert ll.head == node

def test_linked_list_empty():
  ll = LinkedList()
  assert ll.head == None
  
# Make sure to look at the value and not the head
def test_insert_to_empty_linked_list():
  ll = LinkedList()
  ll.insert('apple')
  assert ll.head.value == 'apple'

# This is an O(1) because youre only adding something to the head and not going through the list
def test_insert_to_full_linked_list():
  ll = LinkedList()
  # node 1 apple
  # apple.next = pear
  node1 = Node('apple')
  # ll.head =apple
  ll.head == node1
  # node 2 pear
  # pear.next = None
  node2 = Node('pear')
  # [apple] -> [pear] -> None
  node1.next = node2
  # [banana] -> [apple] -> [pear]
  ll.insert('banana')
  assert ll.head.value == 'banana'
  
def test_multiple_insert_to_full_linked_list():
  ll = LinkedList()
  # node 1 apple
  # apple.next = pear
  node1 = Node('apple')
  # ll.head =apple
  ll.head == node1
  # node 2 pear
  # pear.next = None
  node2 = Node('pear')
  # [apple] -> [pear] -> None
  node1.next = node2
  # [banana] -> [apple] -> [pear]
  ll.insert('banana')
  ll.insert('orange')
  assert ll.head.value == 'orange'
  
def test_head():
  ll = LinkedList()
  assert ll.head == None

def test_include_true():
  ll = LinkedList()
  node1 = Node('Master Chief')
  ll.head = node1
  node2 = Node('Cortana')
  node1.next = node2
  node3 = Node('Noble 6')
  node2.next = node3
  assert ll.include('Noble 6') == True
  
def test_include_false():
  ll = LinkedList()
  node1 = Node('Master Chief')
  ll.head = node1
  node2 = Node('Cortana')
  node1.next = node2
  node3 = Node('Noble 6')
  node2.next = node3
  assert ll.include('Atriox') == False
  
# def test_to_string():
#   ll = LinkedList()
#   node1 = Node('Master Chief')
#   ll.head = node1
#   node2 = Node('Cortana')
#   node1.next = node2
#   node3 = Node('Noble 6')
#   node2.next = node3
#   assert ll.to_string() == "Master Chief -> Cortana -> Noble 6 -> NULL"
  
def test_to_string_revision():
  ll = LinkedList()
  node1 = Node('Master Chief')
  ll.head = node1
  node2 = Node('Cortana')
  node1.next = node2
  node3 = Node('Noble 6')
  node2.next = node3
  assert ll.to_string_revision() == "Master Chief -> Cortana -> Noble 6 -> NULL"
