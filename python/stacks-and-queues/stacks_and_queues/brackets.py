from stacks_and_queues.node import Node
from stacks_and_queues.queue import Queue
from stacks_and_queues.stack import Stack

def validate_brackets(string):
  open_brackets = ['(', '{', '[', '<']
  closed_brackets = [')', '}', ']', '>']
  validated = True
  temp_stack = Stack()
  if string[0] == ')' or string[0] == ']' or string[0] == '}' or string[0] == '>':
    validated = False
    return validated
  else:
    for i in string:
      if i in open_brackets:
        temp_stack.push(i)
      elif i in closed_brackets:
        closed = closed_brackets.index(i)
        if open_brackets[closed] == temp_stack.top.value:
          temp_stack.pop()
        else:
          validated = False
          return validated 
    if temp_stack.isEmpty() == True and validated == True:
      print('I should not do this yet')
      return validated
    
    
  # This was my first version
  # if string[0] == ')' or string[0] == ']' or string[0] == '}' or string[0] == '>':
  #   validated = False
  #   return validated
  # else:
  #   for i in string:
  #     if i in '(' or i == '[' or i == '{' or i == '<':
  #       print(i)
  #       print('I have pushed')
  #       temp_stack.push(i)
  #     elif i == ')' or i == ']' or i == '}' or i == '>':
  #       print(f'I popped on: {i} ')
  #       popped = temp_stack.pop()
  #       print(f'popped: {popped} ')
  #       if popped != '(' or i == '[' or i == '{' or i == '<':
  #         validated = False
  #         return validated 
  #   if temp_stack.isEmpty() == True and validated == True:
  #     print('I should not do this yet')
  #     return validated
