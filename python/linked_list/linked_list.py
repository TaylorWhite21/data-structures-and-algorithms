# Linked List only knows the reference to the head node
class LinkedList:
    def __init__(self, head=None):
        self.head = head
    
    def insert(self, value):
    #Insert creates a new node at the head
    # ll head of 1
    # 1 -> 2 -> None
    # insert 3
    # ll will know the head is 3
    # 3 -> 1 -> 2 -> None
        node = Node(value) # Creates a new node (3) for example above
        # if statement can be removed by setting default value of head to None
        # if self.head is not None:
        
        node.next = self.head # This knows what the old head is because thats what we started with. This will break if the linked list is empty. Fixed by making it an if statement.
        
        self.head = node # Sets this new node as the head
        
    # https://www.geeksforgeeks.org/search-an-element-in-a-linked-list-iterative-and-recursive/
    def include(self, value):
    # Linked list ends when current = none
        current = self.head
        # Searches linked list for the given value
        while current:
            if current.value == value:
                return True
            current = current.next
        return False
    
    # Did it like this because I couldnt figure out how to add different variables to different parts of the string
    # def to_string(self):
    #     current = self.head
    #     node1 = 'empty'
    #     node2 = 'empty'
    #     node3 = 'empty'
    #     stringified = ''
    #     while current:
    #         if node1 == 'empty':
    #             print(f"{current.value}")
    #             node1 = current.value
    #         elif node2 == 'empty':
    #             node2 = current.value
    #         elif node3 == 'empty':
    #             node3 = current.value
                
    #         # stringified += f"{current.value}"
    #         current = current.next
    #         stringified = f"{node1} -> {node2} -> {node3} -> NULL"
    #     print(stringified)
    #     return stringified
    
    
    # Figured it out!!!!!!!!!!!!!
    # https://ao.ms/convert-a-linkedlist-to-a-string-in-python/
    def to_string_revision(self):
        current = self.head
        stringified = ''
        
        while current:
            stringified += '{} -> '.format(current.value)
            current = current.next
        return stringified + 'NULL'
    

class Node:
# Default next to none so that you dont have to worry about ending the list
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
