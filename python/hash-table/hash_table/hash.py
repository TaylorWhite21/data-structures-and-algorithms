from hash_table.linkedlist import LinkedList

class Hashtable:
    def __init__(self, size=1024):
        self.size = size
        self.bucket = size * [LinkedList() for i in range(1024)]

        # Initializer

    def set(self, key, value):

        # Add
        # Arguments: key, value
        # Returns: nothing
        # This method should hash the key, and set the key and value pair in the table, handling collisions as needed.
        # Should a given key already exist, replace its value from the value argument given to this method.
      map_index = self.hash(key)
      bucket = self.bucket[map_index]
      bucket.insert({'key':key, 'value':value})


    def get(self, key):
      index = self.hash(key)
      bucket = self.bucket[index]
      current = bucket.head
      while current:
        value = current.value
        if value['key'] == key:
          return value['value']
        current = current.next
        
      else:
        return None
        # get
        # Arguments: key
        # Returns: Value associated with that key in the table
        

    def contains(self, key):
      index = self.hash(key)
      bucket = self.bucket[index]
      current = bucket.head
      while current:
        value = current.value
        if value['key'] == key:
          return True
        current = current.next
        
      else:
        return None
        # contains
        # Arguments: key
        # Returns: Boolean, indicating if the key exists in the table already.

    def hash(self, key):
        ascii_sum = 0

        for ch in key:
          ascii_sum += ord(ch)
        primed = ascii_sum * 199
        index = primed % self.size
        return index

    def keys(self, table):
      pass
      # current = table.head
      # while current:
      #   value = current.value
      #   if value['key'] == key:
      #     return True
      #   current = current.next
        
      # else:
      #   return None

        # keys
        # Returns: Collection of keys
