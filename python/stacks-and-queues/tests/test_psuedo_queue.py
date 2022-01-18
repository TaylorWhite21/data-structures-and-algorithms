from stacks_and_queues.node import Node
from stacks_and_queues.psuedoqueue import PsuedoQueue
from stacks_and_queues.stack import Stack, CustomStackError
from stacks_and_queues.queue import Queue
from stacks_and_queues.node import Node
import pytest

def test_empty_psuedoqueue():
  psuedo = PsuedoQueue()
  assert psuedo.temp_stack.top == None

def test_node_creation():
  node = Node('Cloud')
  assert node.value == 'Cloud'
  
def test_enqueue():
  psuedo = PsuedoQueue()
  node1_value = 'Tifa'
  psuedo.enqueue(node1_value)
  assert psuedo.final_stack.top.value == 'Tifa'
  
def test_enqueue_multiple():
  psuedo = PsuedoQueue()
  node1_value = 'Sephiroth'
  node2_value = 'Cloud'
  psuedo.enqueue(node1_value)
  psuedo.enqueue(node2_value)
  assert psuedo.final_stack.top.value == 'Cloud'
  
def test_dequeue():
  psuedo = PsuedoQueue()
  node1_value = 'Yuffie'
  node2_value = 'Vincent'
  psuedo.enqueue(node1_value)
  psuedo.enqueue(node2_value)
  assert psuedo.dequeue() == 'Vincent'
  
def test_dequeue_multiple():
  psuedo = PsuedoQueue()
  node1_value = 'Cait Sith'
  node2_value = 'Zack'
  psuedo.enqueue(node1_value)
  psuedo.enqueue(node2_value)
  psuedo.dequeue()
  psuedo.dequeue()
  assert psuedo.final_stack.top == None
  
def test_dequeue_empty_PsuedoQueue():
  empty_psuedo = PsuedoQueue()
  with pytest.raises(CustomStackError):
    empty_psuedo.dequeue()
