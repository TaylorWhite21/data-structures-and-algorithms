from stacks_and_queues.node import Node

class Stack:
  def __init__(self, top=None):
      self.top = top

  def push(self, value):
    node = Node(value)
    node.next = self.top
    self.top = node

    
  def pop(self):
    # current = self.top.value
    # print(f'current before loop: {current}')
    # while current:
      try:
        temp = self.top
        self.top = temp.next
        temp.next = None
        # current = current.next
        # print(f'current after loop: {current}')
        return temp.value

      except:
        raise Exception("You cannot pop an empty list")

  def peek(self):
    if self.isEmpty() == False:
      return self.top.value
    else:
      raise Exception("You cannot peek an empty list")

  def isEmpty(self):
    return self.top == None
