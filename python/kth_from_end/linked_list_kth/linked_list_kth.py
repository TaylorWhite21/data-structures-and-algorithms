class LinkedList:
  def __init__(self, head=None):
        self.head = head
        
  def kth_from_end(self, k):
      if k < 0:
        raise Exception('Negative integers cannot be used')
    
      elif k == 1:
        return self.head
      
      elif self.head is None:
        raise Exception('Linked list is empty')
      current = self.head
      kth = self.head
      
      for _ in range(k):
        if current is None:
          raise Exception('Kth is longer than linked list')
        current = current.next

      while current.next:
        current = current.next
        k = kth.next
      return kth.value

class Node:
  def __init__(self, value, next=None):
        self.value = value
        self.next = next
