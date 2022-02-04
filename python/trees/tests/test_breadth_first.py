from trees.bt_and_bst import BinaryTree
from trees.bt_node import Node
from trees.queue import Queue
from trees.breadth_first import breadth_first

def test_empty_queue():
  empty_q = Queue()
  print('I am in the test')
  assert empty_q.isEmpty() == True

def test_enqueue_one_node():
  node = Node('Garrus')
  bt = BinaryTree(node)
  assert breadth_first(bt) == ['Garrus']
  
def test_enqueue_left_of_root():
  node1 = Node('Miranda')
  node2 = Node('Shepard')
  bt = BinaryTree(node1)
  node1.left = node2
  assert breadth_first(bt) == ['Miranda', 'Shepard']

def test_enqueue_right_of_root():
  node1 = Node('Miranda')
  node2 = Node('Shepard')
  bt = BinaryTree(node1)
  node1.right = node2
  assert breadth_first(bt) == ['Miranda', 'Shepard']
