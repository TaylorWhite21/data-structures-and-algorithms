from stacks_and_queues.node import Node
from stacks_and_queues.stack import Stack


class PsuedoQueue:
  def __init__(self):
    self.temp_stack = Stack()
    self.final_stack = Stack()

  def enqueue(self, value):
    self.temp_stack.push(value)
    self.final_stack.push(self.temp_stack.pop())
  
  def dequeue(self):
    return self.final_stack.pop()
    
