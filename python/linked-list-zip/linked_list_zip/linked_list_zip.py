class LinkedList:
  def __init__(self, head=None):
    self.head = head
    
  # Got help from Marie Marcos(TA) and followed along with Roger
  
  def append(self, prev_node, value):
    # current = self.head
    new_node = Node(value)
    new_node.next = prev_node.next
    prev_node.next = new_node
    
    # while current != None:
    #   print('im in the loop')
    #   if current.next == None:
    #     node.next = None
    #     current.next = node
    #   else:
    #     self.head = Node(value)
    #     print('Im in the else')
  
  # @staticmethod
  def merge_linked_lists(self, list_1, list_2):
    ll_3 = LinkedList()
    current1 = list_1.head
    current2 = list_2.head
    
    while current1 or current2:
      if current1:
        ll_3.append(current1)
        # to do:
        current1 = current1.next
        
      if current2:
        ll_3.append(current2)
        current2 = current2.next

    return ll_3

class Node:
  # Default next to none so that you dont have to worry about ending the list
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
        
    def __repr__(self):
      return f'Node: {self.value}'

def merge_linked_lists(list_1, list_2):
  ll_3 = LinkedList()
  
  ll_3.head = list_1.head
  ll_3.head.next = list_2.head
  
  current1 = list_1.head
  current2 = list_2.head
  
  while current1 or current2:
    print('im in the while loop')
    if current1:
      print("im in the if of the while loop")
      # ll_3.append(current1.value)
      # current1 = current1.next

    if current2:
      print("im in the 2nd if of the while loop")
      # ll_3.append(current2.value)
      # current2 = current2.next
  
  return ll_3
