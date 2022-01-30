from trees.bt_node import Node

class BinaryTree:
  def __init__(self, root=None):
    self.root = root
    
  def pre_order(self):
    # root > left > right
    #           A
    #       /       \
    #      B         C
    #   /    \     /   
    #  D     E    F   
    # Expect A B D E C F
    # empty list for values
    pre_order_list = []
    def walk(root):
      if root is None:
        return
      
      pre_order_list.append(root.value)
      walk(root.left)
      walk(root.right)
    walk(self.root)
    return pre_order_list
    
  
  def in_order(self):
    # left > root > right
    in_order_list = []
    def walk(root):
      if root is None:
        return
      walk(root.left)
      in_order_list.append(root.value)
      walk(root.right)
    walk(self.root)
    return in_order_list
    
  def post_order(self):
    # left > right > root
    post_order_list = []
    def walk(root):
      if root is None:
        return
      walk(root.left)
      walk(root.right)
      post_order_list.append(root.value)
    walk(self.root)
    return post_order_list
  
  class BinarySearchTree:
    def __init__(self, root=None):
      self.root = root
      
    def add(self, value:int):
      node = Node(value)
      if self.root is None:
        self.root = node
      
      def walk(root):
        if self.root.value == node.value:
          return print(f'{node.value} already exists')

        if node.value < root.value:
          if root.left is None:
            root.left = node
          elif root.left.value < node.value:
            node.left = root.left
            root.left = node
          else:
            walk(root.left)
            
        elif node.value > root.value:
          if root.right is None:
            root.right = node
          elif root.right.value > node.value:
            node.right = root.right
            root.right = node
          else:
            walk(root.right)  
      walk(self.root)  
            


    def contains(self, value):
      print(f'root value: {self.root.value}')
      if self.root.value == value:
        return True
      else:
        def walk(root, value):
          print(f'root value in walk: {self.root.value}')
          if root.value == value:
            return True
          elif value < root.value: 
              print(f'root value in less than: {self.root.value}')
              walk(root.left, value)
          elif value > root.value:
              print(f'root value in greater than: {self.root.value}')
              walk(root.right, value)
          else:
            return False
        walk(self.root, value)
