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
  
  def find_max(self):
    if not self.root :
      raise Exception("The tree is empty")
    max_value = self.root.value
    print(f'max value: {max_value}')
    def walk(root, current_max):
      # print(f'root in walk: {root.value}')
      if not root:
        # print(f'root is none: {root.value}')
        print(f'current max: {current_max}')
        return current_max
      if root.value > current_max:
        print(f'root value: {root.value}')
        current_max = root.value
        print(f'current max in if statement: {current_max}')
      current_max = walk(root.left, current_max)
      print(f'current max for left: {current_max}')
      current_max = walk(root.right, current_max)
      print(f'current max for right: {current_max}')
    max_value = walk(self.root, max_value)
    print(f'max value: {max_value}')
    return max_value
  
  # Worked with Roger and he provided solution code
  # def find_max(self):
  #   if not self.root:
  #       raise ValueError("Empty Tree")
  #   max_val = self.root.value
  #   def traverse(root, max_so_far):
  #       # nonlocal max_val
  #       if not root:
  #           return max_so_far
  #       if root.value > max_so_far:
  #           # max_val = root.value
  #           max_so_far = root.value
  #       max_so_far = traverse(root.left, max_so_far)
  #       max_so_far = traverse(root.right, max_so_far)
  #   max_val = traverse(self.root, max_val)
  #   return max_val

  # def find_max(self):
  #   if self.root is None:
  #     return
  #   def walk(root, max_left=0, max_right=0):
  #     if root is None:
  #       return
  #     if root.left:
  #       if root.left.value > max_left:
  #         print(f'root left: {root.left.value}')
  #         max_left = walk(root.left, max_left, max_right)
  #         return max_left
  #     if root.right:
  #       if root.right.value > max_right:
  #         print(f'root right: {root.right}')
  #         max_right = walk(root.right, max_left, max_right)
  #         return max_right
  #     print(f'max_right: {max_right}')
  #     print(f'max_left: {max_left}')
  #     if max_left > max_right:
  #       actual_max = max_left
  #     elif max_right > max_left:
  #       actual_max = max_right
  #     return actual_max
  #   walk(self.root)
      
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
          if root is None:
            print(f'root value in walk: {self.root.value}')
            return
          if root.value == value:
            return True
          elif value < root.value:
              print(f'root value in less than: {self.root.value}')
              return walk(root.left, value)
              
          elif value > root.value:
              print(f'root value in greater than: {self.root.value}')
              return walk(root.right, value)
          else:
            return False
        return walk(self.root, value)
      
