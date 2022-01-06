class LinkedList:
  def __init__(self, head=None):
    self.head = head
    
  # Got help from Marie Marcos(TA) and followed along with Roger
  
  def append(self, value):
    current = self.head
    node = Node(value)
    while current:
      if current.next == None:
        node.next = None
        current.next = node
  
  # @staticmethod
  def merge_linked_lists(self, list_1, list_2):
    ll_3 = LinkedList()
    current1 = list_1.head
    current2 = list_2.head
    
    while current1 or current2:
      if current1:
        ll_3.append(current1)
        current1 = current1.next
        
      if current2:
        ll_3.append(current2.value)
        current2 = current2.next

    return ll_3

class Node:
  # Default next to none so that you dont have to worry about ending the list
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
