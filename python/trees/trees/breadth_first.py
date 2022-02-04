import queue
from re import X
from trees.bt_and_bst import BinaryTree
from trees.bt_node import Node
from trees.queue import Queue

def breadth_first(tree):
  queue = Queue()
  queue.enqueue(tree.root)
  print(f'root value: {tree.root.value}')
  tree_values = []
  count = 0
  
  while  queue.isEmpty() is False:
    count+=1
    print(f'count: {count}')
    print(f'Q front: {queue.front.value}')
    front_node = queue.dequeue()
    print(f'Q rear: {queue.rear}')
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

