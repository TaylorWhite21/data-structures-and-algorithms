from trees.bt_and_bst import BinaryTree
from trees.bt_node import Node
from trees.queue import Queue

def breadth_first(tree):
  queue = Queue()
  tree_values = []
  
  if tree.root is None:
    raise Exception('Tree is empty')
  queue.enqueue(tree.root)
  count = 0
  
  while not queue.isEmpty():
    count+=1
    print(f'count: {count}')
    print(f'Q front: {queue.front.value}')
    print(f'Q rear: {queue.rear}')
    
    front_node = queue.dequeue()
    tree_values.append(front_node.value)
    
    if front_node.left is not None:
      print('I am in the left if')
      queue.enqueue(front_node.left)
      print(queue.isEmpty())

    if front_node.right is not None:
      print('I am in the right if')
      queue.enqueue(front_node.right)
      print(queue.isEmpty())
  return tree_values
