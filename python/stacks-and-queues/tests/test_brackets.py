from stacks_and_queues.brackets import validate_brackets
from stacks_and_queues.node import Node
from stacks_and_queues.stack import Stack

  
def test_closed_brackets_first():
  actual = validate_brackets(']')
  expected = False
  assert actual == expected
  
def test_single_open_and_closed_brackets():
  actual = validate_brackets('()')
  expected = True
  assert  actual == expected
  
def test_double_open_and_closed_brackets():
  actual = validate_brackets('(())')
  expected = True
  assert actual == expected

def test_brackets_with_letters():
  actual = validate_brackets('{}{Code}[Fellows](())')
  expected = True
  assert actual == expected

def test_not_balanced():
  actual = validate_brackets('(](')
  expected = False
  assert actual == expected
  
