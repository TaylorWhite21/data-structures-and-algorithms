from graph.node import Node

class CustomStackError(Exception):
  pass

class Stack:
  def __init__(self, top=None):
      self.top = top

  def push(self, value):
    node = Node(value)
    node.next = self.top
    self.top = node

  def pop(self):
      try:
        temp = self.top
        self.top = temp.next
        temp.next = None
        return temp.value

      except:
        raise CustomStackError("You cannot pop an empty list")

  def peek(self):
    if self.isEmpty() == False:
      return self.top.value
    else:
      raise CustomStackError("You cannot peek an empty list")

  def isEmpty(self):
    return self.top == None
