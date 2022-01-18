from stacks_and_queues.node import Node
from stacks_and_queues.stack import Stack, CustomStackError
from stacks_and_queues.queue import Queue, CustomError
import pytest


# def test_node_creation():
#     node = Node('Erin')
#     assert node.value == 'Erin'

# # Can successfully instantiate an empty stack
# def test_stack_creation():
#     stack = Stack()
#     assert stack.top == None

# # Can successfully push onto a stack
# def test_stack_push():
#     stack = Stack()
#     node_value = 'Inosuke'
#     stack.push(node_value)
#     assert stack.top.value == 'Inosuke'

# # Can successfully push multiple values onto a stack
# def test_stack_push_multiple():
#     stack = Stack()
#     node1_value = 'Toph'
#     node2_value = 'Iroh'
#     node3_value = 'Aang'
#     stack.push(node1_value)
#     stack.push(node2_value)
#     stack.push(node3_value)
#     assert stack.top.value == 'Aang'

# # Can successfully pop off the stack
# def test_stack_pop():
#     stack1 = Stack()
#     node1_value = 'Madara'
#     node2_value = 'Obito'
#     stack1.push(node1_value)
#     stack1.push(node2_value)
#     stack1.pop()
#     assert stack1.top.value == 'Madara'

# # Can successfully empty a stack after multiple pops
# def test_stack_pop_multiple():
#     stack_pop = Stack()
#     node1_value = 'Goku'
#     node2_value = 'Vegeta'
#     node3_value = 'Piccolo'
#     stack_pop.push(node1_value)
#     stack_pop.push(node2_value)
#     stack_pop.push(node3_value)
#     stack_pop.pop()
#     stack_pop.pop()
#     stack_pop.pop()
#     assert stack_pop.top == None


# # Can successfully peek the next item on the stack
# def test_peek_after_push():
#     stack_push_peek = Stack()
#     node1_value = 'Tanjiro'
#     stack_push_peek.push(node1_value)
#     assert stack_push_peek.peek() == 'Tanjiro'

# # Calling pop or peek on empty stack raises exception
# def test_peek_empty():
#     stack_peek = Stack()
#     with pytest.raises(CustomStackError):
#         stack_peek.peek()

# # Can successfully enqueue into a queue
# def test_enqueue():
#     que_test = Queue()
#     node1_value = 'Deku'
#     que_test.enqueue(node1_value)
#     assert que_test.rear.value == 'Deku'

# # Can successfully enqueue multiple values into a queue
# def test_enqueue_multiple():
#     test_multiple = Queue()
#     node1_value = 'Uravity'
#     node2_value = 'Bakugo'
#     node3_value = 'Todoroki'
#     test_multiple.enqueue(node1_value)
#     test_multiple.enqueue(node2_value)
#     test_multiple.enqueue(node3_value)
#     assert test_multiple.rear.value == 'Todoroki'


# # Can successfully dequeue out of a queue the expected value
# def test_dequeue():
#     deque_test = Queue()
#     node1_value = 'Asta'
#     deque_test.enqueue(node1_value)
#     assert deque_test.dequeue() == 'Asta'

# # Can successfully peek into a queue, seeing the expected value
# def test_queue_peek():
#     peek_test = Queue()
#     node1_value = 'Yuno'
#     peek_test.enqueue(node1_value)
#     assert peek_test.peek() == 'Yuno'
    

# # Can successfully empty a queue after multiple dequeues
# def test_dequeue_multiple_true():
#     deque_test = Queue()
#     node1_value = 'Asta'
#     node2_value = 'Yuno'
#     node3_value = 'Yami'
#     deque_test.enqueue(node1_value)
#     deque_test.enqueue(node2_value)
#     deque_test.enqueue(node3_value)
#     deque_test.dequeue()
#     deque_test.dequeue()
#     deque_test.dequeue()
    
#     assert deque_test.isEmpty() == True

# # Can successfully instantiate an empty queue
# def test_empty_queue():
#     empty_queue = Queue()
#     assert empty_queue.isEmpty() == True

# # Calling dequeue or peek on empty queue raises exception
# def test_raise_on_empty():
#     empty_queue = Queue()
#     with pytest.raises(CustomError):
#         empty_queue.peek()

