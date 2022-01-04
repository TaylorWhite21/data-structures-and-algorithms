class LinkedList:
  def __init__(self, head=None):
    self.head = head
  
  def  merge_linked_lists(list_1, list_2):
    new_list = Node()
    tail = new_list
    
    while list_1 != None and list_2 != None:
      tail.next = list_1
      tail = list_1
      list_1 = list_1.next
      
      tail.next = list_2
      tail = list_2
      list_2 = list_2.next
    return new_list.next

class Node:
  # Default next to none so that you dont have to worry about ending the list
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
