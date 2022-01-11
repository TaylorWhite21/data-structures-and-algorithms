from stacks_and_queues import __version__
from stacks_and_queues import stack
from stacks_and_queues.node import Node
from stacks_and_queues.stack import Stack


def test_node_creation():
    node = Node('Erin')
    assert node.value == 'Erin'

# Can successfully instantiate an empty stack
def test_stack_creation():
    stack = Stack()
    assert stack.top == None

# Can successfully push onto a stack
def test_stack_push():
    stack = Stack()
    node_value = 'Inosuke'
    stack.push(node_value)
    assert stack.top.value == 'Inosuke'

# Can successfully push multiple values onto a stack
def test_stack_push_multiple():
    stack = Stack()
    node1_value = 'Toph'
    node2_value = 'Iroh'
    node3_value = 'Aang'
    stack.push(node1_value)
    stack.push(node2_value)
    stack.push(node3_value)
    assert stack.top.value == 'Aang'

# Can successfully pop off the stack
def test_stack_pop():
    stack1 = Stack()
    node1_value = 'Madara'
    node2_value = 'Obito'
    stack1.push(node1_value)
    stack1.push(node2_value)
    stack1.pop()
    assert stack1.top.value == 'Madara'

# Can successfully empty a stack after multiple pops
def test_stack_pop_multiple():
    stack_pop = Stack()
    node1_value = 'Goku'
    node2_value = 'Vegeta'
    node3_value = 'Piccolo'
    stack_pop.push(node1_value)
    stack_pop.push(node2_value)
    stack_pop.push(node3_value)
    stack_pop.pop()
    stack_pop.pop()
    stack_pop.pop()
    assert stack_pop.top == None


# Can successfully peek the next item on the stack
def test_peek_after_push():
    stack_push_peek = Stack()
    node1_value = 'Tanjiro'
    stack_push_peek.push(node1_value)
    assert stack_push_peek.peek() == 'Tanjiro'

# Calling pop or peek on empty stack raises exception
def test_peek_empty(self):
    stack_peek = Stack()
    stack_peek.peek()
    self.assertRaises(Exception)


# Can successfully enqueue into a queue
# Can successfully enqueue multiple values into a queue
# Can successfully dequeue out of a queue the expected value
# Can successfully peek into a queue, seeing the expected value
# Can successfully empty a queue after multiple dequeues
# Can successfully instantiate an empty queue
# Calling dequeue or peek on empty queue raises exception
