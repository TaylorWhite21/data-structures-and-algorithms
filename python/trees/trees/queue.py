from trees.node import Node

class CustomError(Exception):
  pass

class Queue:
  def __init__(self, front=None, rear=None):
    self.front = front
    self.rear = rear
    
  def enqueue(self, value):
    node = Node(value)
    if self.rear is None:
      self.front = node
      self.rear = node
    else:
      self.rear.next = node
      self.rear = self.rear.next

  def dequeue(self):
    if self.front is None:
      raise CustomError('Queue is empty')
    else:
        temp = self.front
        self.front = temp.next
        temp.next = None
    return temp.value

  def peek(self):
    if self.front is None:
      raise CustomError('Queue is empty')
    else:
      return self.front.value
    
  def isEmpty(self):
    return self.front == None
