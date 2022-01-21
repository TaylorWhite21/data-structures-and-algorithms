from stacks_and_queues.node import Node
from stacks_and_queues.queue import Queue
from stacks_and_queues.stack import Stack
from stacks_and_queues.animal import Animal
import pytest

def test_shelter_enqueue():
  que_test = Animal()
  node1_value = 'cat'
  que_test.enqueue(node1_value)
  assert que_test.rear.value == 'cat'

def test_shelter_enqueue_mulitple():
  que_test = Animal()
  node1_value = 'cat'
  node2_value = 'dog'
  node3_value = 'cat'
  que_test.enqueue(node1_value)
  que_test.enqueue(node2_value)
  que_test.enqueue(node3_value)
  assert que_test.front.value == 'cat'
  assert que_test.front.next.value == 'dog'
  assert que_test.front.next.next.value == 'cat'

def test_shelter_dequeue_cat_in_front():
  que_test = Animal()
  node1_value = 'cat'
  node2_value = 'dog'
  node3_value = 'cat'
  que_test.enqueue(node1_value)
  que_test.enqueue(node2_value)
  que_test.enqueue(node3_value)
  assert que_test.dequeue('cat') == 'cat'

def test_shelter_dequeue_cat_not_front():
  que_test = Animal()
  node1_value = 'dog'
  node2_value = 'dog'
  node3_value = 'cat'
  que_test.enqueue(node1_value)
  que_test.enqueue(node2_value)
  que_test.enqueue(node3_value)
  assert que_test.dequeue('cat') == 'cat'
  
def test_shelter_dequeue_dog_in_front():
  que_test = Animal()
  node1_value = 'dog'
  node2_value = 'dog'
  node3_value = 'cat'
  que_test.enqueue(node1_value)
  que_test.enqueue(node2_value)
  que_test.enqueue(node3_value)
  assert que_test.dequeue('dog') == 'dog'

def test_shelter_dequeue_dog_not_front():
  que_test = Animal()
  node1_value = 'cat'
  node2_value = 'cat'
  node3_value = 'dog'
  que_test.enqueue(node1_value)
  que_test.enqueue(node2_value)
  que_test.enqueue(node3_value)
  assert que_test.dequeue('dog') == 'dog'

def test_pref_not_dog_or_cat():
  que_test = Animal()
  node1_value = 'cat'
  node2_value = 'Nina'
  que_test.enqueue(node1_value)
  que_test.enqueue(node2_value)
  assert que_test.dequeue('Nina') == None
