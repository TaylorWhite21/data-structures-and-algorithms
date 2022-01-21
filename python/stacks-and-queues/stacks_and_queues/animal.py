from stacks_and_queues.node import Node
from stacks_and_queues.queue import Queue
from stacks_and_queues.stack import Stack

class CustomError(Exception):
  pass

class Animal:
  def __init__(self, cat=None, dog=None, front=None, rear=None):
    self.cat = cat
    self.dog = dog
    self.front = front
    self.rear = rear
    self.temp_stack = Stack()
    
  def enqueue(self, animal):
    node = Node(animal)
    if self.rear is None:
      self.front = node
      self.rear = node
    else:
      self.rear.next = node
      self.rear = self.rear.next

  def dequeue(self, pref):
    if self.front is None:
      raise CustomError('Queue is empty')
    elif pref == 'cat':
      if self.front.value == 'cat':
        temp = self.front
        self.front = temp.next
        temp.next = None
        return temp.value 
      else:
        while self.front.value is not 'cat':
          temp = self.front
          self.front = temp.next
          self.temp_stack.push(temp.value)
          if self.front.value == 'cat':
            found_cat = self.front.value
            while self.temp_stack is not None:
              self.enqueue(self.temp_stack.pop())
              return found_cat
    elif pref == 'dog':
      print(f'pref: {pref}')
      if self.front.value == 'dog':
        temp = self.front
        self.front = temp.next
        temp.next = None
        return temp.value 
      else:
        while self.front.value is not 'dog':
          temp = self.front
          self.front = temp.next
          self.temp_stack.push(temp.value)
          if self.front.value == 'dog':
            found_dog = self.front.value
            while self.temp_stack is not None:
              self.enqueue(self.temp_stack.pop())
              return found_dog
    else:
      return None
